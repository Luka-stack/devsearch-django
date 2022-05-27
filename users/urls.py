from django.urls import path
from . import views

urlpatterns = [
    path('login/', view=views.login_user, name='login'),
    path('logout/', view=views.logout_user, name='logout'),
    path('register/', view=views.register_user, name='register'),

    path('', view=views.profiles, name='profiles'),
    path('profile/<str:pk>/', view=views.user_profile, name='user-profile')
]
