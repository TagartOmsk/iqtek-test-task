from service import service
from model import schemas

from fastapi import FastAPI

app = FastAPI()


@app.get('/users', response_model=schemas.User)
async def get_user_by_id(user_id: int):
    return service.get_user(user_id)


@app.post('/users')
async def add_user(user: schemas.UserCreate):
    return service.create_user(user)


@app.put('/users/update')
async def update_user(user: schemas.User):
    return service.update_user(user.user_id, user)


@app.delete('/users/delete')
async def delete_user(user_id: int):
    return service.delete_user(user_id)
