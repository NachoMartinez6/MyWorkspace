
# Importamos la libreria de fastapi -> pip install fastapi[all]  
from fastapi import FastAPI



# Creamos una instancia de FastAPI, es una clase que nos permitirá acceder a determinadas funciones.
app = FastAPI()



@app.get("/")
async def root():
    return {"body": {
        "status_code": 200,
        "message": "Hola FastAPI!"
    }}
