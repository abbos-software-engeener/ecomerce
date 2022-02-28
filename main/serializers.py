from rest_framework import serializers
from .models import *


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post_Comment
        fields = "__all__"


class PostCommentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post_Comment
        fields = "__all__"
        depth = 2


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
