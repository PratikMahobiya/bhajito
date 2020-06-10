from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()

class AuthBackend(ModelBackend):
    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False
    
    def authenticate(self, request, username=None, password=None):
        print('inside custom auth')
        try:
            user = User.objects.get(username=username)
            print("anderwala",user)#for testing purpose
            return user
        except User.DoesNotExist:
            return None