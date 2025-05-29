from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

# Update database URI for Heroku
if os.environ.get('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL'].replace("postgres://", "postgresql://")

# Configure for Heroku
if os.environ.get('PORT'):
    app.config['PORT'] = int(os.environ.get('PORT', '5002'))
    app.config['SERVER_NAME'] = os.environ.get('SERVER_NAME')

# Initialize database
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    organization = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print(f"Database initialization error: {str(e)}")

# Routes remain the same as before

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/demo')
def demo():
    return render_template('contact_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']
        organization = request.form['organization']
        message = request.form['message']

        contact = Contact(
            name=name,
            email=email,
            organization=organization,
            message=message
        )
        db.session.add(contact)
        db.session.commit()

        flash('Thank you for your interest! We have received your request.')
        return redirect(url_for('demo'))
    except Exception as e:
        error_msg = f'An error occurred while processing your request: {str(e)}'
        flash(error_msg)
        return redirect(url_for('demo'))

@app.route('/health')
def health_check():
    return jsonify(status="healthy", timestamp=datetime.utcnow())

@app.route('/view-contacts')
def view_contacts():
    contacts = Contact.query.order_by(Contact.timestamp.desc()).all()
    return render_template('contacts.html', contacts=contacts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
