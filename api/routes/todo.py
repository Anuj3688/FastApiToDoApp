from fastapi import APIRouter, HTTPException,status
from api.models.todo import Todo
from api.schemas.todo import GetTodo, PutTodo, PostTodo

todo_router = APIRouter(prefix="/api", tags=['todo'])

@todo_router.get("/")
async def all_todo():
    data = Todo.all()
    return await GetTodo.from_queryset(data)

@todo_router.post("/")
async def post_todo(body:PostTodo):
    row = Todo.create(**body.dict(exclude_unset=True))
    return await GetTodo.from_tortoise_orm(row)

@todo_router.put("/{key}")
async def update_todo(key: int,body:PutTodo):
    data = body.dict(exclude_unset=True)
    exist = await Todo.filter(id=key).exists()
    if not exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Todo not found")
    await Todo.filter(id=key).update(*data)
    return await GetTodo.from_queryset_single(Todo.get(id=key))


@todo_router.delete("/{key}")
async def delete_todo(key: int):
    exist = await Todo.filter(id=key).exists()
    if not exist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Todo not found")
    await Todo.filter(id=key).delete()
    return "Todo Deleted success fully"
