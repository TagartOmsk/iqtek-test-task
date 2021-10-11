from model import schemas


class RAMDB:
    data = {}
    last_id = 0

    def __init__(self):
        pass

    def add(self, user: schemas.UserCreate):
        self.last_id += 1
        user.user_id = self.last_id
        self.data.update({self.last_id: user})
        return self.last_id

    def get(self, user_id):
        return self.data.get(user_id)

    def update(self, user_id, user: schemas.User):
        # assuming it's always PUT, thus just replace the old user instance with a new one
        if user_id in self.data:  # if user already exists just update it
            self.data.update({user_id: user})
        else:  # if specified user_id doesn't exist in db - create new user and return it's corresponding user_id
            return None

        return user_id

    def delete(self, user_id):
        if self.data.get(user_id) is None:
            return
        del self.data[user_id]
