# Pet-Website
Konrad Koc  kok20002

Ashley Negron amn20017

Mikael Daluz mcd21017

Von Lindenthal vml21004

Trello Board Link: https://trello.com/b/uu1cemtE/cse2102-project

Figma Prototype Link: https://www.figma.com/proto/vge47by7dz4RJa5QVwpjz1/CSE-2102-Project-Prototype?node-id=0-1&t=dOAkwKwEU7wwRfE0-1

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Running with Docker](#running-with-docker)
- [API Reference](#api-reference)
- [Database Schema](#database-schema)
- [Development Workflow](#development-workflow)
- [Troubleshooting](#troubleshooting)
- [Current Work / In Progress](#current-work--in-progress)
- [Future Improvements](#future-improvements)

---

## Overview

The Pet Adoption Platform provides:

- A RESTful backend API built with Flask
- User authentication and account management
- Pet listings with filtering and saving functionality
- Persistent storage with SQLite
- Dockerized deployment for consistent environments

The goal of this project is to demonstrate:

- API design
- Backend architecture
- Containerization
- Developer-focused documentation
- Maintainable project structure

---

## Features

### User Features
- Create account
- Login / authentication
- Save favorite pets
- View saved pets list

### Pet Features
- Browse pets
- Fetch pet details
- Filter by attributes
- Persist pet data

### Developer Features
- REST API
- Swagger documentation
- Docker support
- Local development environment
- Modular backend structure

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Flask |
| Database | SQLite |
| API Docs | Swagger |
| Containerization | Docker |
| Language | Python 3.10+ |
| Version Control | Git/GitHub |

---

## Architecture

### High Level Flow

```text
Frontend (React)
        ↓
Flask REST API
        ↓
SQLite Database

---

## Project Structure Backend
1. Git clone our repo
   
   `git clone <https://github.uconn.edu/CSE2102-Spring25/CSE2102-Spring25-Team16.git>`

2. Use a vm for this to run
   
   `python3 -m venv venv`

   `source venv/bin/activate`

3. Go into backend directory

   `cd backend`

4. Install dependencies

   `pip install -r requirements.txt`

5. Initialize the DB
   
   `python init_db.py`

6. Run the Backend API Server (or run from docker, steps below)
   
   `python main.py`

- http://127.0.0.1:5000 <- server address
- /api/pets <- pets
- /api/users <- users
- /apidocs <- Swagger UI doc

### Troubleshooting  
If port already in use:  
`lsof -i :5000`
`kill -9 <pid>`


### Docker

(run from root and vm)

`docker build -t team16-backend ./backend`

`docker run -p 5000:5000 team16-backend`



### API Endpoints Summary

| Endpoint | Method | Description |
|-------------|---------|----------|
| `/api/users` | `GET` | Get all users
| `/api/register` | `POST` | Register a user
| `/api/login` | `POST` | Login with email
| `/api/profile` | `GET/PUT` | Get or update profile (user ID 1 for demo)
| `/api/pets` | `GET` | Get all pets
| `/api/pets/search?species=cat` | `GET` | Filter pets by species
| `/api/pets/<id>` | `GET` | Get pet by ID
| `/api/pets/<id>/save` | `POST` | Save pet
| `/api/pets/saved` | `GET` |  Get saved pets
| `/apidocs` | `GET` | Swagger UI interactive docs

(`/api/pets/<id>/save` and `/api/pets/saved`  have full functionality)

---

## Frontend Structure (check Doceker below)

1. Navigate to the frontend directory

`cd frontend`

2. Install dependencies (only run once)

`npm install`

3. Start the development server:

`npm start`

### Docker Setup

run with vm

Build Docker image 

From the `/frontend` directory: `docker build -t pet-frontend .`

Run it

`docker run -p 3000:3000 pet-frontend`

---

## Database Schema

### Users
| Column | Type | 
|-------------|---------|
| `id` | `int` |
| `username` | `text` |
| `email` | `text` |
| `password` | `text` | 

### Pets
| Column | Type | 
|-------------|---------|
| `id` | `int` |
| `name` | `text` |
| `species` | `text` | 
| `breed` | `text` |
| `age` | `int` |
| `allergen` | `text` |
| `temperament` | `text` |
| `owner_id` | `int` |
| `image` | `text` |

### Saved Pets
| Column | Type | 
|-------------|---------|
| `id` | `int` |
| `user_id` | `int` |
| `pet_id` | `int` | 

### Events
 | Column | Type | 
|-------------|---------|
| `id` | `int` |
| `name` | `text` |
| `date` | `text` | 

### Events
 | Column | Type | 
|-------------|---------|
| `id` | `int` |
| `user_id` | `int` |
| `event_id` | `int` | 

### Database reset

`rm database.db`  
`python backend/init_db.py`

---

## Future Improvements

JWT authentication

Pagination

Deployment to cloud provider

Logging + monitoring integration

API versioning

Unit tests




