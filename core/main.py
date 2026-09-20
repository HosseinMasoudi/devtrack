from fastapi import FastAPI

app = FastAPI(description="DevTrack is a production-oriented project management backend built with FastAPI.")

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

