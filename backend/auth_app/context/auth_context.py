from auth_app.strategies.email_password import EmailPasswordStrategy

class AuthContext:
    
    strategies = {
        'email': EmailPasswordStrategy(),
    }

    @classmethod
    def set_strategy(cls, auth_type):
        return cls.strategies.get(auth_type, None)
    
    @classmethod
    def authenticate(cls, auth_type, data):
        strategy = cls.get_strategy(auth_type)

        if not strategy:
            raise ValueError("Invalid authentication method")
        
        return strategy.authenticate(data)