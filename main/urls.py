from django.urls import path
from .views import *

urlpatterns = [
    path('post_comment/', PostCommentView.as_view()),
    path('post_comment/<int:pk>/', PostCommentView.as_view()),
    path('contact/', CantactView.as_view()),
    path('contact/<int:pk>/', CantactView.as_view()),
]