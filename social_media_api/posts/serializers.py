
from rest_framework import serializers

from django_blog.blog.models import Comment
from social_media_api.posts.models import Post, LikeModel


# Make sure the person posting is authenticated
class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source ="post.author")

    class Meta:
        model = Post
        fields = "__all__"



class CommentSerializer(serializers.ModelSerializer):
    author= serializers.ReadOnlyField(source ="comment.author")

    class Meta:
        model = Comment
        fields = "__all__"



class LikeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source ="like.author")

    class Meta:
        model = LikeModel
        fields = "__all__"




