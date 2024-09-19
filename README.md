# Smart-Vision - WORK IN PROGRESS

## Overview

**Smart Vision** is an AI-powered system designed to assist Alzheimer's and Age-related Macular Degeneration (AMD) patients by providing real-time object recognition and environmental hazard detection. The system uses AI models developed in TensorFlow, optimized for low-power hardware, and delivers fast and accurate pill and item recognition, even under low-light conditions.

Key features include:
- 95% accuracy in pill and item recognition.
- 75% faster processing than previous prototypes.
- Real-time object detection at 30 frames per second on low-power hardware.
- Low-light detection functional at 10 lux.
- Identification and distinction of over 1,000 pill types.
- Response time under 1 second for hazard detection.

## Tech Stack

### Frontend
- **React.js** for the user interface.
- **Service Workers** for offline capabilities (PWA).
  
### Backend
- **Python (Flask/FastAPI)** for server-side processing and API.
- **TensorFlow** for AI model development and inference.
- **SQL/NoSQL** database for managing user and object data.
  
### AI & Models
- **TensorFlow** for deep learning models.
- Custom-trained models for pill identification and object recognition.
- Real-time processing with optimizations for low-power hardware.

## Project Structure

```
smart-vision/
├── .git/                           # Git version control folder
├── .gitignore                      # Files and folders to ignore by Git
├── README.md                       # Project overview and setup instructions
├── LICENSE                         # License information for the project
├── requirements.txt                # Python dependencies for backend and AI
├── package.json                    # Node.js dependencies and project info
├── client/                         # Frontend application
│   ├── public/                     # Static assets (HTML, images, icons)
│   │   ├── index.html              # Main HTML file
│   │   ├── favicon.ico             # App favicon
│   │   └── manifest.json           # Web app manifest for PWA
│   ├── src/                        # React source files
│   │   ├── components/             # Reusable React components
│   │   ├── pages/                  # Page components (Home, About, etc.)
│   │   ├── hooks/                  # Custom hooks for state management
│   │   ├── styles/                 # CSS/SASS stylesheets
│   │   ├── utils/                  # Utility functions (API calls, etc.)
│   │   ├── contexts/               # Context API for state management
│   │   ├── App.js                  # Main app component
│   │   ├── index.js                # Entry point for React
│   │   ├── serviceWorker.js        # Service worker for PWA
│   │   └── setupTests.js           # Test setup for Jest
│   └── tests/                      # Frontend tests
│       ├── App.test.js             # Tests for App component
│       └── other tests...          # Other component tests
├── server/                         # Backend application
│   ├── app/                        # Main app logic
│   │   ├── controllers/            # Request handlers for API
│   │   ├── models/                 # Database models (ORM, schema)
│   │   ├── routes/                 # API route definitions
│   │   ├── services/               # Business logic and service functions
│   │   ├── middlewares/            # Middleware functions (auth, logging)
│   │   ├── config/                 # Configuration files (database, environment vars)
│   │   ├── utils/                  # Utility functions (validation, formatting)
│   │   ├── server.py               # Main entry point for the server
│   │   ├── error_handlers.py        # Error handling for APIs
│   │   └── test.py                 # Test script for backend
│   └── tests/                      # Backend tests
│       ├── controllers.test.py     # Tests for controllers
│       ├── models.test.py          # Tests for models
│       ├── routes.test.py          # Tests for routes
│       └── integration.test.py      # Integration tests for API
├── ai/                             # AI model and processing
│   ├── models/                     # Pre-trained models and custom models
│   │   ├── model.py                # AI model definition
│   │   ├── train.py                # Training script
│   │   ├── evaluate.py             # Evaluation script
│   │   └── export_model.py         # Script to export trained model
│   ├── data/                       # Data files for training and testing
│   │   ├── dataset/                # Raw dataset
│   │   ├── processed/              # Processed dataset
│   │   └── annotations/            # Annotations for training
│   ├── inference/                  # Inference logic
│   │   ├── object_detection.py      # Object detection script
│   │   ├── low_light_detection.py   # Low-light detection logic
│   │   ├── medication_recognition.py # Medication distinction algorithms
│   │   └── real_time_processing.py  # Real-time processing scripts
│   └── requirements.txt            # Python dependencies for AI models
├── tests/                          # Integration and end-to-end tests
│   ├── e2e/                        # End-to-end test cases
│   │   └── e2e.test.js             # Test script for end-to-end testing
│   ├── unit/                       # Unit tests for various components
│   │   ├── client.test.js          # Unit tests for client-side
│   │   ├── server.test.js          # Unit tests for server-side
│   │   └── ai.test.py              # Unit tests for AI models
├── scripts/                        # Utility scripts for development
│   ├── setup_db.py                 # Script to set up the database
│   ├── run_migrations.py           # Script to run database migrations
│   ├── seed_data.py                # Script to seed the database with initial data
│   └── clear_data.py               # Script to clear the database
└── docs/                           # Documentation for the project
    ├── architecture.md             # Architecture overview
    ├── setup.md                    # Setup instructions for developers
    ├── api.md                      # API documentation (endpoints, requests, responses)
    ├── user_manual.md              # User manual for the app
    └── testing.md                  # Testing guidelines and best practices

```