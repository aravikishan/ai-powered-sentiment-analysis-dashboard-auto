# AI-Powered Sentiment Analysis Dashboard

## Overview
The AI-Powered Sentiment Analysis Dashboard is a robust application designed to provide real-time sentiment analysis of textual data. Leveraging the power of FastAPI, this tool offers a seamless experience for users looking to extract sentiment insights from various text inputs. Whether you're a business seeking to understand customer feedback, a researcher analyzing public opinion, or a developer needing sentiment data integration, this dashboard serves as a comprehensive solution. It provides a user-friendly interface for immediate sentiment analysis, tracks historical data for trend analysis, and offers API endpoints for easy integration into other applications.

## Features
- **Real-time Sentiment Analysis**: Quickly analyze the sentiment of text inputs and receive instantaneous feedback.
- **Intuitive Dashboard**: Navigate through a well-designed interface that simplifies the sentiment analysis process.
- **Historical Data Tracking**: Review past sentiment analyses to identify patterns and trends over time.
- **Comprehensive API Documentation**: Detailed documentation of API endpoints for seamless integration into other systems.
- **Responsive Design**: Access the dashboard on various devices with a mobile-friendly layout.
- **Customizable Analysis Parameters**: Tailor sentiment analysis settings to meet specific requirements.

## Tech Stack
| Technology       | Version  |
|------------------|----------|
| Python           | 3.11+    |
| FastAPI          | 0.95.2   |
| Uvicorn          | 0.22.0   |
| Jinja2           | 3.1.2    |
| Pydantic         | 1.10.7   |
| SQLite           | Built-in |

## Architecture
The project is architected to separate concerns between the backend and frontend, ensuring a clean and maintainable codebase. The backend, powered by FastAPI, manages API requests and database interactions. The frontend, built with Jinja2 templates, provides a dynamic and interactive user interface.

### Project Structure
```plaintext
ai-powered-sentiment-analysis-dashboard-auto
│
├── app.py                # Main application file containing API logic
├── Dockerfile            # Docker configuration for containerization
├── requirements.txt      # Python dependencies
├── start.sh              # Script to start the application
├── static/               # Static files (CSS, JS)
│   ├── css/
│   │   └── style.css    # Styling for the application
│   └── js/
│       └── main.js      # Client-side scripts
├── templates/            # HTML templates
│   ├── analysis.html    # Analysis page template
│   ├── api_docs.html    # API documentation page template
│   ├── history.html     # History page template
│   └── home.html        # Home page template
└── sentiment_analysis.db # SQLite database file
```

### Data Flow
```plaintext
User Input -> FastAPI Endpoint -> Sentiment Analysis -> Database Storage -> Response to User
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-powered-sentiment-analysis-dashboard-auto.git
   cd ai-powered-sentiment-analysis-dashboard-auto
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database (if not already created):
   ```bash
   python app.py
   ```

### Running the Application
Start the application using Uvicorn:
```bash
uvicorn app:app --reload
```
Visit `http://localhost:8000` in your web browser to access the dashboard.

## API Endpoints
| Method | Path                  | Description                                              |
|--------|-----------------------|----------------------------------------------------------|
| GET    | `/`                   | Returns the home page.                                   |
| GET    | `/analysis`           | Returns the sentiment analysis page.                     |
| GET    | `/history`            | Returns the history page.                                |
| GET    | `/api-docs`           | Returns the API documentation page.                      |
| POST   | `/api/analyze`        | Analyzes the sentiment of provided text.                 |
| GET    | `/api/history`        | Returns a list of past sentiment analysis results.       |
| GET    | `/api/history/{id}`   | Returns details of a specific sentiment analysis result. |

## Project Structure
```
ai-powered-sentiment-analysis-dashboard-auto
│
├── app.py                # Main application file containing API logic
├── Dockerfile            # Docker configuration for containerization
├── requirements.txt      # Python dependencies
├── start.sh              # Script to start the application
├── static/               # Static files (CSS, JS)
│   ├── css/
│   │   └── style.css    # Styling for the application
│   └── js/
│       └── main.js      # Client-side scripts
├── templates/            # HTML templates
│   ├── analysis.html    # Analysis page template
│   ├── api_docs.html    # API documentation page template
│   ├── history.html     # History page template
│   └── home.html        # Home page template
└── sentiment_analysis.db # SQLite database file
```

## Screenshots
*Placeholder for screenshots showcasing the dashboard interface and features.*

## Docker Deployment
To build and run the application using Docker:
1. Build the Docker image:
   ```bash
   docker build -t sentiment-analysis-dashboard .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 sentiment-analysis-dashboard
   ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.

---
Built with Python and FastAPI.
