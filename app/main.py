from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'status':True,'message':"Todo Api's are running"}