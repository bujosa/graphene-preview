users = '''
     {
         users(first: 2){
             username
             lastLogin
         }
     }
    '''

createUser = '''
    mutation createUser($username: String){
        createUser(username: $username){
            user{
                username
            }
        }
    }
    '''