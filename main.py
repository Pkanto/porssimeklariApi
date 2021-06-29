from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from datetime import date
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine
from pydantic import BaseModel
from models import Ilmoitus


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class Ilmoitus_teko(BaseModel):
    nimi : str
    aika : date
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

templates = Jinja2Templates(directory = "templates")


@app.get("/")
async def ilmoitustaulu(request: Request):
    return templates.TemplateResponse("ilmoitustaulu.html", {
        "request": request,
        "somevar":2
    })

@app.post('/ilmoitus')

def ilmoituksen_teko(ilmoituksen_teko: Ilmoitus_teko, db: Session = Depends(get_db)):
    ilmoitus = Ilmoitus()
    ilmoitus.aika = ilmoituksen_teko.aika
    ilmoitus.nimi = ilmoituksen_teko.nimi

    db.add(ilmoitus)
    db.commit()
    return{
        "koodi":"Luonti onnistui",
        "viesti": "osake luotu"
    }