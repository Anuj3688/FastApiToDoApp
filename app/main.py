from fastapi import FastAPI
from api.routes.todo import todo_router
from tortoise.contrib.fastapi import register_tortoise
app = FastAPI()
app.include_router(todo_router)

register_tortoise(
    app=app,
    db_url="sqlite://todo.db",
    add_exception_handlers=True,
    generate_schemas=True,
    modules={"models":["api.models.todo"]}
)
@app.get('/')
def index():
    return {'status':True,'message':"Todo Api's are running"}