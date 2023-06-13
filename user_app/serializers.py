# imports from rest_framework and django
from rest_framework import serializers
from django.contrib.auth.models import User


#imports from user_app
from user_app.models import Profile 


class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['email'] = instance.user.email

        return representation