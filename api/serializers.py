from rest_framework import serializers
from api.models import Author,Post

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), source='author', write_only=True)

    class Meta:
        model = Post
        fields = "__all__"

    def get_author(self, obj):
        return AuthorSerializer(obj.author).data