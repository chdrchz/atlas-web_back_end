# User Authentication Service

This project implements a simple user authentication service in Python using Flask. While it's recommended in the industry to use existing frameworks or modules (such as Flask-User) for authentication, this project serves as an educational tool to build the system from scratch, understanding the fundamental concepts behind authentication.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Routes](#api-routes)
- [License](#license)

## Project Overview

In this project, you will learn how to build a basic authentication system from the ground up using Flask. The focus is on understanding how authentication works and interacting with APIs in a Flask app without relying on pre-built modules for handling authentication.

### Features

- User registration and login
- Session management using cookies
- Retrieving request form data for authentication
- Setting and getting cookies
- Handling various HTTP status codes

## Learning Objectives

By the end of this project, you should be able to explain the following concepts:

- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.9)
- Your code should use the `pycodestyle` style (version 2.5)
- You should use `SQLAlchemy` for database interactions
- Flask app should only interact with the `Auth` class, not directly with the database
- All public methods should have proper documentation

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/savdavis/user-authentication-service.git

   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask App:
   ```bash
   flask run
   ```

## API Routes

- POST /register: Registers a new user
- POST /login: Logs in a user and sets a session cookie
- GET /profile: Retrieves user profile (requires authentication)
- POST /logout: Logs out a user and clears the session cookie

## License

This project is licensed under the MIT License.
