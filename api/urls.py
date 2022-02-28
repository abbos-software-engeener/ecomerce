from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('category/',CategoryView.as_view()),
    path('category/<int:pk>/',CategoryView.as_view()),
    path('product/',ProductView.as_view()),
    path('product/<int:pk>/',ProductView.as_view()),
    path('card/', CardView.as_view()),
    path('card/<int:pk>/', CardView.as_view()),
    path('order/', OrderView.as_view()),
    path('order/<int:pk>/', OrderView.as_view()),
    path('orderproduct/', OrderProductView.as_view()),
    path('orderproduct/<int:pk>/', OrderProductView.as_view()),
]
