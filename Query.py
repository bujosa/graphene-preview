import graphene
import User
from datetime import datetime

user = User.User

class UserQuery(graphene.ObjectType):
    users = graphene.List(user, first=graphene.Int())

    def resolve_users(self, info, first):
        return [
            user(username='Test1', lastLogin=datetime.now()),
            user(username='Test2', lastLogin=datetime.now()),
            user(username='Test3', lastLogin=datetime.now())
        ][:first]