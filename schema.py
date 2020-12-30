import graphene
import Query 

schema = graphene.Schema(query=Query.UserQuery)

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