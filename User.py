import graphene

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    lastLogin = graphene.Date()