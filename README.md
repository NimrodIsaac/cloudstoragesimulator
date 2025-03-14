# Cloud Storage Simulator

A Flask-based web application that simulates a basic cloud storage system. This application allows users to upload, view, update, and delete files with a modern and responsive interface.

## Features

- File upload simulation
- View list of stored files
- Update file names
- Delete files
- Modern and responsive UI using Bootstrap
- Flash messages for user feedback

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <your-github-repo-url>
cd cloud-storage-simulator
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Deployment to Vercel

1. Create a `vercel.json` file in the root directory with the following content:
```json
{
    "version": 2,
    "builds": [
        {
            "src": "app.py",
            "use": "@vercel/python"
        }
    ],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "app.py"
        }
    ]
}
```

2. Install Vercel CLI:
```bash
npm install -g vercel
```

3. Deploy to Vercel:
```bash
vercel
```

4. Follow the prompts to complete the deployment.

## Project Structure

```
cloud-storage-simulator/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── static/
│   └── style.css      # Custom CSS styles
├── templates/
│   └── index.html     # Main HTML template
└── README.md          # Project documentation
```

## Technologies Used

- Flask
- Bootstrap 5
- Python
- Vercel (for deployment)

## License

This project is open source and available under the MIT License. 