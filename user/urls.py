from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('registration/',views.RegistrationView.as_view()),
    path("me/", views.MeView.as_view(), name="me"),
    path('login/', views.UserLogin.as_view(), name="login"),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('search/', views.SearchUserView.as_view(), name="search")
]