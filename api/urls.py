from rest_framework.routers import DefaultRouter
from api.views import AuthorViewSet, PostViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
