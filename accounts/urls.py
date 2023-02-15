from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login-user/", views.login_user, name="login_user"),
    path("register/", views.register, name="register"),
]