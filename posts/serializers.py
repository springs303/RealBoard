from rest_framework import serializers
from users.serializers import ProfileSerializer
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    ###
    profile = ProfileSerializer(read_only=True) 
    # nested serializer
    # Meta 클래스에서 profile이 pk만 나오는 것이 아닌 전체 정보를 출력하도록 해줌
    ### 
    class Meta:
        model = Post
        fields = ("pk","author","profile","title","body","image","published_date","likes")

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "category", "body", "image")

class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only = True)

    class Meta:
        model = Comment
        fields = ("pk","profile","post","text")

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("title","category","body","image")