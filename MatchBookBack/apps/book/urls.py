from django.urls import path, include
from .views import BookViewsSet, ListBookUserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', BookViewsSet, basename='book')


urlpatterns = [
    path('', include(router.urls)),
    path('user-books/<uuid:pk>', ListBookUserViewSet.as_view()),
] + router.urls


