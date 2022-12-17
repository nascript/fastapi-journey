from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': 'Nasution'}}

@app.get('/about')
def about():
    return {'data': {'name': 'aboutpage'}}
