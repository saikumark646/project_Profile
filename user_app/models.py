from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
phone_regex = RegexValidator(
    regex=r"^\+\d{2,3}\-\d{9,11}$",
    message="format: '+91-9999999999'. Up to 15 digits allowed.",
)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,db_index=True)
    first_name = models.CharField(max_length=10, null=True, blank=True)
    last_name = models.CharField(max_length=10, null=True, blank=True)
    bio = models.CharField(max_length=20000, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile/',null=True, blank=True)
    contact = models.CharField(validators=[phone_regex],
                               max_length=15, blank=True, null=True
                               )
    
    @property
    def name(self):
        return f"{self.first_name}_{self.last_name}"

    def __str__(self):
        return f'{str(self.user.username)}'
