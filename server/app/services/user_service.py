class UserService:
    def __init__(self):
        self.users = []  # In-memory storage for demonstration

    def create_user(self, data):
        user_id = len(self.users) + 1
        user = {**data, 'id': user_id}
        self.users.append(user)
        return user

    def get_user(self, user_id):
        for user in self.users:
            if user['id'] == user_id:
                return user
        return None