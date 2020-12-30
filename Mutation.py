import graphene
import User
from datetime import datetime

UserType = User.User

class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()

    user = graphene.Field(UserType)

    def mutate(self, info, username):
        user = UserType(username = username)
        return CreateUser(user=user)

class UserMutation(graphene.ObjectType):
    create_user = CreateUser.Field()