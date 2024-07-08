from rest_framework.viewsets import ModelViewSet
from api.serializers import AuthorSerializer,PostSerializer
from api.models import Author,Post

class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
