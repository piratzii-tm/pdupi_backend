# Practica dezvoltării unui proiect IT → Backend Repo

### How to run it?
1. Create a virtual environment: `python3 -m venv venv/`
2. Start the environment: 
   - `source venv/bin/activate` (Mac) 
   - `.\venv\Scripts\activate.bat` (Windows)
3. Install the requirements: `pip install -r requirements.txt`
4. Add the python interpreter from the virtual environment (PyCharm).
5. Start the server by running: `uvicorn main:app --reload` 

### What it contains?
This repo contains the default database (containing mocked data) and the FastAPI application defining the backend handling of the GymFit web application. 

The backend handling contains a router, service, repository and model file for each concept the application is using. Each of these concepts (and other necessary models) have their own route and folder present in `/src`.

The basic routes for each concept are mentioned below, but for more details see `./assets/fastapi_swagger_ui.pdf` or run the server and access `http://127.0.0.1:8000/docs`:
1. `/client`
2. `/gym_class`
3. `/trainer`
4. `/admin`
