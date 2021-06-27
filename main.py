from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates 

app = FastAPI()
templates = Jinja2Templates(directory = "templates")


@app.get("/")
async def ilmoitustaulu(request: Request):
    return templates.TemplateResponse("ilmoitustaulu.html", {
        "request": request,
        "somevar":2
    })

@app.post('/osake')

def luo_osake():
    return{
        "koodi":"Luonti onnistui",
        "viesti": "osake luotu"
    }