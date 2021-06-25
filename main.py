from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/osake')

def luo_osake():
    return{
        "koodi":"Luonti onnistui",
        "viesti": "osake luotu"
    }