from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from authy.views import UserProfile, EditProfile

urlpatterns = [
    # Profile Section
    
    path('profile/edit', EditProfile, name="editprofile"),
 path('create_event/', views.create_event, name='create_event'),
    path('events/', views.events, name='events'),
    # User Authentication
    path('sign-up/', views.register, name="sign-up"),
    path('signin/', auth_views.LoginView.as_view(template_name="signin.html", redirect_authenticated_user=True), name='sign-in'),
   
    path('sign-out/', auth_views.LogoutView.as_view(template_name="sign-out.html"), name='sign-out'), 
]
