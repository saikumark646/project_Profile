from django.core.validators import validate_email
from rest_framework import permissions


from user_app.models import Profile



def validate_email_address(email):
    validate_email(email)
                

class IsUserAuthOrSameUser(permissions.BasePermission):
    def has_permission(self,request,obj):
        user_id = Profile.objects.get(id=obj.kwargs.get('pk')).user_id
        param = False
        if request.method in permissions.SAFE_METHODS:
            param =  True
        elif user_id == self.request.user.id:
            param = True
        return param