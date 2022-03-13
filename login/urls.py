from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', views.login_view, name="login"),
    path('accounts/logout', views.logout_view, name="logout"),
    path("signup/", views.SignUp.as_view(), name="signup"),
]
