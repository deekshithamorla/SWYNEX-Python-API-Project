# SWYNEX-Python-API-Project
A simple Python REST API project built using Flask with validation and error handling.
# SWYNEX Python API Project

This project is a simple REST API built using Python and Flask.

## Features

- Flask-based REST API
- GET endpoint for checking API status
- POST endpoint for adding two numbers
- Input validation
- Error handling
- JSON responses

## Endpoints

### GET /

Returns the API status.

### POST /add

Adds two numbers.

Example request:

{
  "a": 10,
  "b": 20
}

Example response:

{
  "a": 10,
  "b": 20,
  "result": 30
}

## Technologies Used

- Python
- Flask
- REST API
- JSON

## How to Run

Install the required package:

pip install -r requirements.txt

Run the application:

python app.py