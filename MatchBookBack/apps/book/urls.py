from django.urls import path, include
from .views import BookSerializer
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', BookSerializer, basename='book')


urlpatterns = [
    path('', include(router.urls)),
] + router.urls
