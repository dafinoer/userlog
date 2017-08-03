from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class EmailBackend(object):
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
            if getattr(user, 'is_active', False) and user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None


    def get_user(self, user_id):
        print (user_id)
        cls_user = get_user_model()
        try:
          return cls_user.objects.get(pk=user_id)
        except cls_user.DoesNotExist:
          return None
