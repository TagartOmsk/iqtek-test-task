from pydantic import BaseModel  # the package is used for data validation inside of model classes


class UserBase(BaseModel):
    user_id: int
    last_name: str
    first_name: str
    middle_name: str = None  # may be missing


class UserCreate(UserBase):
    pass


class User(UserBase):
    pass

    class Config:
        orm_mode = True
