# MediChateX
## AI-Powered Personalized Medicine Recommendation System

The **MediChateX** is a full-stack application designed to manage **medicine prescriptions**, **patient data**, and **ML-powered predictions**. It consists of:
- A **Flask backend** for handling API requests, integrating machine learning models, and managing patient data.
- A **React.js frontend** for the web, providing a user-friendly interface to interact with the backend.
- A **React Native mobile app** that allows users to access the platform from their mobile devices.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Backend](#backend)
- [Frontend](#frontend)
- [Mobile App](#mobile-app)
- [Docker Setup](#docker-setup)
- [How to Run](#how-to-run)
- [License](#license)

## Features

- **Patient Management**: Add, update, and view patient records.
- **Medicine Prediction**: Use machine learning to recommend medication based on the patient’s data.
- **Multi-platform Support**: Accessible via a web app (React.js) and mobile app (React Native).
- **User Authentication**: Login and Signup functionality for both web and mobile users.

## Tech Stack

- **Backend**: Flask, Python, SQLite, Machine Learning (e.g., Scikit-Learn)
- **Frontend**: React.js, JavaScript, HTML, CSS
- **Mobile App**: React Native, JavaScript
- **Database**: SQLite
- **Containerization**: Docker, Docker Compose

## Backend

The backend is built using **Flask**, a lightweight Python framework. It includes an **API** for managing patient data, user authentication, and medicine predictions, powered by a machine learning model.

### Setup

1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd medicine-app/backend

- **app.py**: This is the main Flask application file that handles API requests. It includes routes for user authentication, managing patient records, and recommending medicines using the trained ML model.
  
- **train_model.py**: This script trains the machine learning model using patient data and saves it as `medicine_model.pkl`. The model predicts recommended medicines based on user input.

- **medicine_model.pkl**: The trained machine learning model. It is used by the backend to make predictions on the user's data and recommend relevant medicines.

- **label_encoder.pkl**: The label encoder is used to convert categorical data (e.g., symptoms or conditions) into numerical data that the machine learning model can understand.

- **patients.db**: An SQLite database that stores patient records, including personal details and medical history. This data is used by the backend to make more personalized recommendations.

- **requirements.txt**: This file contains all the Python dependencies required for the backend, including Flask, Scikit-learn, and SQLite.

- **README.md** (Backend): The documentation for the backend, explaining how to set up, run, and interact with the backend.

## Frontend

The frontend is a **React.js** web application that provides a user-friendly interface for interacting with the backend API. It is designed to manage patient records, perform user authentication, and display the recommended medicines.

### Directory Structure

- **public/**: This folder contains static assets like `index.html`, logos, and other images required for the frontend.

- **src/**: This folder contains the source code for the React application.

  - **components/**: This subfolder contains reusable React components that make up different pages and sections of the application.
    - **Login.js**: The component responsible for the login page where users can authenticate.
    - **Signup.js**: The component responsible for the signup page where new users can register.
    - **Navbar.js**: The component that defines the navigation bar used across the app.
    - **Home.js**: The main page where users can input their symptoms to get medicine recommendations.
    - **Results.js**: This page displays the recommended medicines based on the user's input.

  - **App.js**: This is the root component that serves as the main container for the application.

  - **App.css**: The CSS file responsible for styling the React app.

  - **index.js**: The entry point of the React app, where it connects to the DOM and renders the app.

- **package.json**: This file lists the Node.js dependencies required for the frontend, such as React and React Router.

- **README.md** (Frontend): Documentation for setting up and running the React.js frontend.

### Setup

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend


This markdown structure includes all relevant information, proper code formatting, and clear steps for setting up the project. It will display well in the `README.md` file when rendered on platforms like GitHub.

