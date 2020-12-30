import graphene
import query 
import mutation
import schemas

schema = graphene.Schema(query=query.UserQuery, mutation=mutation.UserMutation)

result_query = schema.execute(
    schemas.users
)

result_mutation = schema.execute(
    schemas.createUser, variable_values={'username': "Bujosa"}
)

print(result_query)

print(result_mutation)