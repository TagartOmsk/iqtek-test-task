from model import schemas
from fastapi import HTTPException
from configurer import repo

ERROR_CODE = 400
SUCCESS_CODE = 200


def get_user(user_id: int):
    res = repo.get_user(user_id)  # who
    if res is None:
        raise HTTPException(status_code=ERROR_CODE, detail='User not found')
    return res


def update_user(user_id: int, user: schemas.User):
    res = repo.update_user(user_id, user)
    if res is None:
        raise HTTPException(status_code=ERROR_CODE, detail='User not found')
    return res


def create_user(user: schemas.UserCreate):  # returns new user's user_id
    res = repo.create_user(user)
    return res


def delete_user(user_id: int):
    repo.delete_user(user_id)

