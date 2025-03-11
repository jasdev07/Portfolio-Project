# FastAPI Backend Project(Deploying)

This project is a FastAPI backend service that can be easily set up and deployed by other developers. Below are the instructions for installation and setup.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed [Docker](https://www.docker.com/get-started) and Docker Compose.
- You have a basic understanding of Docker containerization.

## Installation Instructions for local Docker containers

To install the FastAPI Backend Project, follow these steps:

1. Clone the repository:
    bash
        git clone [REPOSITORY_URL] -->

2. Navigate to the project directory:

    cd fastapi_backend

3. To run the FastAPI application, execute:

    docker-compose up --build

4. Verifying the Deployment.
    After running the application, open your web browser and navigate to:

    http://localhost:8081


# Backend API for Frontend Team

This document provides details on the backend API for integration with the frontend application.

## API Endpoint

The primary endpoint for calculations is `/calculate`, which accepts a POST request with multipart form data.

### Request Format# Armas Backend Project Deployment Guide

This project is the `armas_backend` service, a robust FastAPI backend designed for seamless integration and deployment. Below you'll find comprehensive instructions for local setup with Docker and guidelines for frontend integration.

## Prerequisites

- Docker and Docker Compose installed ([Docker](https://www.docker.com/get-started)).
- Familiarity with Docker concepts and containerization principles.

## Local Deployment with Docker

### Installation

1. **Clone the Repository**:
   Clone the Armas Backend repository to your local machine.
   ```bash
   git clone [REPOSITORY_URL]

### Project Setup:
    Change into the project directory:

        cd armas_backend

### Run the Application:
    Launch the FastAPI application with Docker Compose:

        docker-compose up --build

### Verification:
    Confirm the deployment by visiting the following URL in your browser:

        http://localhost:8081/docs

    This will display the Swagger UI for the API, indicating successful deployment.

## Backend API Usage for Frontend Integration

    The backend provides an API with endpoints tailored for frontend interaction, primarily the "/calculate" endpoint for processing and predictions.

### Submitting Calculation Requests
    Endpoint: /calculate
    Method: POST
    Data Format: Multipart Form
    Parameters:
        - Brand: Brand of the motorcycle (e.g., Yamaha).
        - ModelType: Model type (e.g., YZF-R1).
        - ModelFrameworks: Model framework (e.g., independent_model).
        - BrandNewDate: Manufacturing date in ISO 8601 format.
        - RepossessedDate: Repossession date in ISO 8601 format.
        - LeftImageFile: Image file of the left view.
        - RightImageFile: Image file of the right view.
        - FrontImageFile: Image file of the front view.
        - RearImageFile: Image file of the rear view.
        - AudioFile: Audio recording of the motorcycle.

### CORS Configuration for Frontend Access

    To enable communication between the frontend and backend services, configure CORS settings as follows:
        ```python
        from fastapi.middleware.cors import CORSMiddleware

        origins = [
            "http://frontend.dev-domain.com",  # Development Frontend URL
            "https://frontend.production-domain.com",  # Production Frontend URL
        ]

        app.add_middleware
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=[""],
        allow_headers=[""],


    Replace the placeholder URLs with the actual URLs from which your frontend will serve its application.

### Response and Health Check
    The /calculate endpoint will respond with a structured JSON containing the prediction result. Similarly, a GET request to /health ensures the backend's operational status.

    json:
        {
            "ensemble_prediction": "Class A" // This could also be a numerical score or structured object.

        }

    Health Check Response Example

    json:
        {
            "status": "healthy"
        }

## Troubleshooting and Support
    For any integration issues:

    Confirm CORS origins match your frontend's URL.
    Check for typos in environment variables.
    Review Docker logs for backend errors.
    For additional help or to report an issue with the armas_backend, please contact our support team at support@armas_backend.com or file an issue in our GitHub repository.

- `Brand`: String
- `ModelType`: String
- `ModelFrameworks`: String
- `BrandNewDate`: String (ISO 8601 date format)
- `RepossessedDate`: String (ISO 8601 date format)
- `LeftImageFile`: File (image)
- `RightImageFile`: File (image)
- `FrontImageFile`: File (image)
- `RearImageFile`: File (image)
- `AudioFile`: File (audio)

## Configuring CORS for Frontend Integration

### Understanding CORS

CORS (Cross-Origin Resource Sharing) is a security feature in web browsers that restricts web pages from making requests to a different domain than the one that served the web page. This is an important security measure to prevent malicious websites from accessing sensitive data.

However, when developing a web application with separate frontend and backend services, you might need to allow requests from your frontend domain to your FastAPI backend. This is where configuring CORS comes into play.

### Setting Up CORS in FastAPI

In the provided FastAPI application, CORS is configured through the `origins` list. This list defines the URLs that are allowed to communicate with the backend. 

The relevant code snippet in your FastAPI setup looks like this:

```python
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:8082",  # Replace with the actual URL of the front-end application
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

### Configuring the Origins List
Identify Your Frontend URL: Determine the URL from which your frontend application will be served. This might be http://localhost:3000 for local development or a production URL like https://your-frontend-domain.com.

Update the Origins List: Replace "http://localhost:8082" with the URL ofyour frontend application in the origins list. 

Example:
    """
      origins = [
        "http://localhost:3000",  # Local development URL
        "https://your-frontend-domain.com",  # Production URL
    ]
    """
  
If you have multiple environments (like development, staging, and production), you may add each environment's frontend URL to the list.

### Response Format

The API responds with a JSON object containing an `ensemble_prediction` key. The value may be a class name (string), score (numeric), or a complex object, depending on the backend processing.

Example:
    json:
        {
            "ensemble_prediction": "Class A" // or 0.85, or any other structured data
        }


#### API Health Response Format

A GET request to /health will return the application's health status.

{
    "status": "healthy"
}
