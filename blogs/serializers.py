from rest_framework import serializers
from .models import Blog, Comment, CustomUser
from cloudinary.models import CloudinaryField

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
    
class ImageSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ReadOnlyField()

    class Meta:
        model = CustomUser
        fields = ['profile_picture']


class BlogSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)
    profile_picture = ImageSerializer(read_only = True)

    class Meta:
        model = Blog
        fields = ['id', 'username', 'comments', 'body', 'description' ,'date' ,'user', 'profile_picture']

    def get_comments(self, obj):
        comments = obj.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return serializer.data