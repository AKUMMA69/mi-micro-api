from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    texto: str

@app.get("/")
def home():
    return {"status": "API activa y funcionando correctamente"}

@app.post("/v1/procesar")
def procesar_datos(data: InputData):
    resultado = data.texto.strip().upper()
    return {
        "status": "success",
        "longitud": len(resultado),
        "resultado_procesado": resultado
    }
