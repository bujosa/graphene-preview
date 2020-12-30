import graphene
import json 
from datetime import datetime
class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    lastLogin = graphene.Date()

class Query(graphene.ObjectType):
    users = graphene.List(User, first=graphene.Int())

    def resolve_users(self, info, first):
        return [
            User(username='Test1', lastLogin=datetime.now()),
            User(username='Test2', lastLogin=datetime.now()),
            User(username='Test3', lastLogin=datetime.now())
        ][:first]

schema = graphene.Schema(query=Query)

result = schema.execute(
    '''
     {
         users(first: 2){
             id
             username
             lastLogin
         }
     }
    '''
)

print(result)