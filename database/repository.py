from database.ramdb import RAMDB
from database import models
from model import schemas
from sqlalchemy.orm import sessionmaker


class Repository:
    def get_user(self, user_id: int):
        pass

    def update_user(self, user_id: int, user: schemas.User):
        pass

    def create_user(self, user: schemas.UserCreate):
        pass

    def delete_user(self, user_id: int):
        pass


class RAMRepository(Repository):
    def __init__(self, db: RAMDB):
        self.db = db

    def get_user(self, user_id: int):
        return self.db.get(user_id)

    def update_user(self, user_id: int, user: schemas.User):
        return self.db.update(user_id, user)

    def create_user(self, user: schemas.UserCreate):
        return self.db.add(user)

    def delete_user(self, user_id: int):
        self.db.delete(user_id)


class SQLRepository(Repository):
    def __init__(self, session_maker: sessionmaker):
        self.session_maker = session_maker

    def get_user(self, user_id: int):
        db = self.session_maker()
        res = db.query(models.User).filter(models.User.user_id == user_id).first()
        db.close()
        return res

    def update_user(self, user_id: int, user: schemas.User):
        db = self.session_maker()
        db.query(models.User).filter(models.User.user_id == user_id).update({
            'last_name': user.last_name,
            'first_name': user.first_name,
            'middle_name': user.middle_name,
        })
        db.close()
        return user_id

    def create_user(self, user: schemas.UserCreate):

        db_user = models.User(
            last_name = user.last_name,
            first_name = user.first_name,
            middle_name = user.middle_name,
        )

        db = self.session_maker()

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        user_id = db_user.user_id
        db.close()
        return user_id

    def delete_user(self, user_id: int):
        db = self.session_maker()

        db.query(models.User).filter(
            models.User.user_id == user_id
        ).delete()

        db.close()
