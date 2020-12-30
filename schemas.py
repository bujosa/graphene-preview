users = '''
     {
         users(first: 2){
             username
             lastLogin
         }
     }
    '''

createUser = '''
    mutation createeUser{
        createUser(username: "TestBujosa"){
            user{
                username
            }
        }
    }
    '''