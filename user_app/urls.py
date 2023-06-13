from django.urls import path
from user_app.views import CreateUser,UpdateProfile
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('user_create/',CreateUser.as_view())
]

router = SimpleRouter()
router.register(r'profile_update',UpdateProfile,basename='profile_update')

urlpatterns += router.urls