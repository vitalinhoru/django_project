from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, CustomPasswordResetView, VerifyEmailView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify_email/<str:uid>/<str:token>/', VerifyEmailView.as_view(), name='verify_email'),
    # path('register_success/', register_success, name='register_success'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset')
    ]