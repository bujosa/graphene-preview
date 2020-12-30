import graphene
import User
from datetime import datetime

user = User.User

class CreateUser(graphene.Mutation):
    class Arguments:
        
class UserMutation(graphene.ObjectType):
    create_user = CreateUser.Field()