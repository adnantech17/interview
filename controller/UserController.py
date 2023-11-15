from repository import UserRepository
from models import User


class UserController:
    def __init__(self):
        self._userRepository = UserRepository()

    def register(self, email):
        id = len(self._userRepository.getAllUsers()) + 1
        user = User(id, email)
        self._userRepository.addUser(user)
        return {
            'data': user,
            'message': 'Register Success',
            'code': 201,
        }

    def login(self, email):
        user = self._userRepository.getUserByEmail(email=email)
        if user is None:
            return {
                'data': None,
                'message': 'User not found!',
                'code': 401,
            }

        return {
            'data': user,
            'message': 'Login Success',
            'code': 200,
        }
