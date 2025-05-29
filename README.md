# AI Safeguard

## Project Overview

This is a web application for AI Safeguard.

## Deployment

### GitHub Pages

This project is configured to deploy to GitHub Pages. When you push changes to the main branch:

1. The GitHub Actions workflow will run automatically
2. All static files and templates will be copied to the `docs` directory
3. The site will be deployed to GitHub Pages

### Local Development

To run locally:

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

The application will be available at `http://localhost:5000` by default.

## Project Structure

- `/docs` - Contains static files and templates for GitHub Pages
- `/static` - Static assets (CSS, JS, images)
- `/templates` - Flask template files
- `app.py` - Main Flask application
- `requirements.txt` - Python dependencies
- `.github/workflows/pages.yml` - GitHub Actions workflow for deployment

## License

MIT License
