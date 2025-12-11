from auth_app.models.user import User

class UserService:

    @staticmethod
    def create_user(email, password, username=""):
        user = User.objects.create_user(
            email=email,
            password=password,
            username=username
        )

        return user