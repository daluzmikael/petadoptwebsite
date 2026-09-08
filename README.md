# Pet Adoption Portal

Spring 2025 CSE 2102 Team 16 project by Konrad Koc, Ashley Negron, Mikael Daluz, and Von Lindenthal.

The application has a Flask/SQLite API and a React frontend. The API initializes its database automatically, so a clean clone can start without a checked-in database file.

## Run locally

Requirements: Python 3.10 or newer and Node.js 20 or newer.

In the first terminal:

```bash
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

In a second terminal:

```bash
cd frontend
npm ci
npm start
```

Open <http://localhost:3000>. A seeded login is `alice@example.com` with password `password123`, or create a new account.

The frontend uses `http://localhost:5000` by default. Set `REACT_APP_API_URL` before building or starting the frontend when the API is hosted elsewhere. Set `PET_ADOPTION_DB_PATH` to override the backend database location.

## Run with Docker

From the repository root:

```bash
docker compose up --build
```

Then open <http://localhost:3000>. The API and Swagger UI are available at <http://localhost:5000> and <http://localhost:5000/apidocs>.

## Verify

```bash
cd backend
python -m unittest discover -s tests -v

cd ../frontend
npm run build
```

The same checks run in GitHub Actions for pushes and pull requests to `main` and `develop`.

## Main API endpoints

| Endpoint | Method | Description |
| --- | --- | --- |
| `/api/register` | `POST` | Create an account |
| `/api/login` | `POST` | Log in with email and password |
| `/api/pets` | `GET` | List available pets |
| `/api/pets/search?query=cat` | `GET` | Search pet fields |
| `/api/pets/<id>/save` | `POST` | Save a pet for a user |
| `/api/pets/saved/<user_id>` | `GET` | List a user's saved pets |
| `/api/events` | `GET` | List events |
| `/api/events/<id>/rsvp` | `POST`, `DELETE` | Add or remove an RSVP |
| `/api/questionnaire/submit` | `POST` | Save questionnaire answers |
