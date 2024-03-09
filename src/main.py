from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "This is fastapi medium level 2"}