# AI-Based Recommendation Platform

The AI-Based Recommendation Platform is a media recommendation application that allows users to discover and manage various media types such as movies, books, and games. The application is built using FastAPI for the backend and React for the frontend, providing a seamless user experience.

## Project Structure

The project is organized into two main directories: `backend` and `frontend`.

### Backend

The backend is built with FastAPI and includes the following components:

- **app/**: Contains the main application code.
  - **main.py**: Entry point for the FastAPI application, initializes the app and sets up routes.
  - **core/**: Contains configuration and security-related files.
    - **config.py**: Configuration settings, including environment variables and database URLs.
    - **security.py**: Handles authentication, password hashing, and JWT helper functions.
  - **models/**: Defines the database models using SQLAlchemy.
    - **user.py**: User schema.
    - **item.py**: Media item schema.
  - **schemas/**: Contains Pydantic models for request and response validation.
    - **user.py**: User-related Pydantic models.
    - **item.py**: Media item-related Pydantic models.
  - **api/**: Defines the API routes.
    - **routes_users.py**: User authentication endpoints (signup/login).
    - **routes_items.py**: CRUD operations for media items.
    - **routes_recos.py**: Recommendation endpoints.
  - **services/**: Contains business logic and database utilities.
    - **recommender.py**: Machine learning logic for recommendations.
    - **db_utils.py**: Database helper functions.
  - **db.py**: Database engine and session setup.
  - **__init__.py**: Marks the app directory as a Python package.
- **tests/**: Contains unit tests for the application.
  - **test_users.py**: Tests for user authentication functionalities.
  - **test_recos.py**: Tests for recommendation logic.
- **requirements.txt**: Lists the Python dependencies required for the backend.
- **Dockerfile**: Defines the Docker container setup for the backend application.

### Frontend

The frontend is built with React and includes the following components:

- **src/**: Contains the source code for the React application.
  - **components/**: Reusable components for the application.
    - **Navbar.jsx**: Navigation bar component.
    - **Card.jsx**: Reusable card component for displaying media items.
  - **pages/**: Contains the main pages of the application.
    - **Home.jsx**: Dashboard page displaying recommended and trending items.
    - **Login.jsx**: Login page component.
    - **Signup.jsx**: Signup page component.
    - **Profile.jsx**: User profile page, including favorites.
  - **services/**: Contains API service calls.
    - **api.js**: Axios calls to interact with the backend API.
  - **App.jsx**: Root React component that sets up the application structure.
  - **main.jsx**: Entry point for the React application.
- **package.json**: Lists the frontend dependencies and scripts for the project.
- **vite.config.js**: Configuration settings for Vite, the build tool.

### Docker Compose

- **docker-compose.yml**: Orchestrates the backend and frontend services for the application.

## Getting Started

To get started with RecoHub, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd recohub
   ```

2. Set up the backend:
   - Navigate to the `backend` directory.
   - Install the required dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Run the FastAPI application:
     ```
     uvicorn app.main:app --reload
     ```

3. Set up the frontend:
   - Navigate to the `frontend` directory.
   - Install the required dependencies:
     ```
     npm install
     ```
   - Start the React application:
     ```
     npm run dev
     ```

4. Access the application:
   - Open your browser and go to `http://localhost:3000` for the frontend.
   - The backend API will be available at `http://localhost:8000`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License


This project is licensed under the MIT License. See the LICENSE file for more details.
