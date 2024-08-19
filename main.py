from fastapi import FastAPI 

app = FastAPI()

@app.get('/')  #decoration 
def index():
    return {'data':{'name':'suhas'}}

@app.get('/about')  #decoration 
def about():
    return {'data':'about Page'}