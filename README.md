# Pet-Website
Konrad Koc  kok20002

Ashley Negron amn20017

Mikael Daluz mcd21017

Von Lindenthal vml21004

Trello Board Link: https://trello.com/b/uu1cemtE/cse2102-project

Figma Prototype Link: https://www.figma.com/proto/vge47by7dz4RJa5QVwpjz1/CSE-2102-Project-Prototype?node-id=0-1&t=dOAkwKwEU7wwRfE0-1

---

## Project Structure Backend
1. Git clone our repo
git clone <https://github.uconn.edu/CSE2102-Spring25/CSE2102-Spring25-Team16.git>

2. Use a vm(optional)
   
python3 -m venv venv

source venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

6. Initialize the DB(from CSE2102-Spring25-Team16 directory
   
python backend/init_db.py

8. Run the Backend API Server
   
python backend/main.py

- http://127.0.0.1:5000 <- server address
- /api/pets <- pets
- /api/users <- users
- /apidocs <- Swagger UI doc


### Docker

docker build -t teamXX-backend ./backend

docker run -p 5000:5000 teamXX-backend



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

(/api/pets/<id>/save and /api/pets/saved  have full functionality)

---

## Frontend Structure

1. Navigate to the frontend directory

`cd frontend`

2. Install dependencies 

`npm install`

3. Start the development server:

`npm start`
