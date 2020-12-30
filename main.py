import graphene
import Query 

schema = graphene.Schema(query=Query.UserQuery)

result_query = schema.execute(
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

result_mutation = schema.execute(
    '''
    mutation createeUser
    '''
)

print(result_query)

print(result_mutation)