import graphene
import user
from datetime import datetime

User = user.User

class UserQuery(graphene.ObjectType):
    users = graphene.List(User, first=graphene.Int())

    def resolve_users(self, info, first):
        return [
            User(username='Test1', lastLogin=datetime.now()),
            User(username='Test2', lastLogin=datetime.now()),
            User(username='Test3', lastLogin=datetime.now())
        ][:first]