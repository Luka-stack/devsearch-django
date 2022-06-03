from django.urls import path
from . import views

urlpatterns = [
    path('login/', view=views.login_user, name='login'),
    path('logout/', view=views.logout_user, name='logout'),
    path('register/', view=views.register_user, name='register'),

    path('', view=views.profiles, name='profiles'),
    path('profile/<str:pk>/', view=views.user_profile, name='user-profile'),
    path('account/', view=views.user_account, name='user-account'),
    path('edit-account', view=views.edit_account, name='edit-account'),

    path('create-skill', view=views.create_skill, name='create-skill'),
    path('update-skill/<str:pk>/', view=views.update_skill, name='update-skill'),
    path('delete-skill/<str:pk>/', view=views.delete_skill, name='delete-skill'),

]
