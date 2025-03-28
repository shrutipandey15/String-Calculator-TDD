# String Calculator

A Test-Driven Development (TDD) implementation of a String Calculator, built using Python for the backend and React for the frontend.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [API Reference](#api-reference)

---

## Overview
This project implements a String Calculator that takes a string of numbers separated by custom delimiters and computes their sum. It follows TDD principles and includes unit tests for validation. The frontend provides a user-friendly interface for input and result display.

## Features
- Handles default delimiters (`,` and `\n`)
- Supports custom single and multi-character delimiters
- Allows multiple custom delimiters
- Ignores numbers greater than 1000
- Throws an error for negative numbers, listing all found negatives
- Provides a web interface for easy interaction

## Tech Stack
### Backend:
- Python
- Flask
- Regular Expressions (re)
- Poetry for dependency management
- Unit testing with `pytest`

### Frontend:
- React
- CSS (Pico.css for styling)
- Fetch API for backend communication
- Vitest and React Testing Library for frontend testing

## Installation

### Backend Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/shrutipandey15/String-Calculator-TDD
   cd string-calculator/backend
   ```
2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```
3. Run the server:
   ```sh
   poetry run python server.py
   ```
   The backend will start on `http://localhost:5000`.

### Frontend Setup
1. Navigate to the frontend directory:
   ```sh
   cd ../frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the development server:
   ```sh
   npm run dev
   ```
   The frontend will be available at `http://localhost:5173`.

## Usage
1. Enter a string of numbers separated by default (``,` ` or `\n`) or custom delimiters.
2. Click the `Calculate` button.
3. The sum will be displayed unless errors occur.

## Testing

### Backend Testing
Run unit tests for the Python backend using:
```sh
poetry run pytest
```

### Frontend Testing
Run tests for the React frontend:
```sh
npm test
```

## API Reference
### `POST /calculate`
**Request Body:**
```json
{
  "numbers": "//[***]\n1***2***3"
}
```
**Response:**
```json
{
  "result": 6
}
```
**Error Responses:**
- `400 Bad Request` if invalid input is provided

