# Pet-Website
Konrad Koc  kok20002

Ashley Negron amn20017

Mikael Daluz mcd21017

Von Lindenthal vml21004

Trello Board Link: https://trello.com/b/uu1cemtE/cse2102-project

Figma Prototype Link: https://www.figma.com/proto/vge47by7dz4RJa5QVwpjz1/CSE-2102-Project-Prototype?node-id=0-1&t=dOAkwKwEU7wwRfE0-1

---

## Project Structure
1. Git clone our repo
git clone <https://github.uconn.edu/CSE2102-Spring25/CSE2102-Spring25-Team16.git>

2. Use a vm(optional)
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Initialize the DB(from CSE2102-Spring25-Team16 directory
python backend/init_db.py

5. Run the Backend API Server
python backend/main.py

- http://127.0.0.1:5000 <- server address
- /api/pets <- pets
- /api/users <- users
- /apidocs <- Swagger UI doc


Docker
docker build -t teamXX-backend ./backend
docker run -p 5000:5000 teamXX-backend

---
API Endpoints Summary

| Endpoint | Method | Description |
|-------------|---------|
| `/api/users` | All Python scripts for each stage of the project (modularized) |
| `/api/register` | Cleaned and split datasets (train/test) |
| `/api/login` | Fine-tuned BERT models and tokenizers |
| `/api/profile` | Confusion matrix visualizations |
| `/api/pets` | Jupyter notebook version of full pipeline (optional) |
| `/api/pets/search?species=cat` | Project overview and documentation |
| `/api/pets/<id>` | All Python scripts for each stage of the project (modularized) |
| `/api/pets/<id>/save` | All Python scripts for each stage of the project (modularized) |
| `/api/pets/saved` | All Python scripts for each stage of the project (modularized) |
| `/apidocs` | All Python scripts for each stage of the project (modularized) |

