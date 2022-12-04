from django.urls import path, include
from .views import BookViewsSet, ListBookUserViewSet, BookApiViewSet, BookApiUserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', BookViewsSet, basename='book')


urlpatterns = [
    path('', include(router.urls)),
    path('user-books/<uuid:pk>', ListBookUserViewSet.as_view()),
    path('books-api/<str:name>/', BookApiViewSet.as_view({'get': 'info'})),
    path('books-api/user/<str:id>/', BookApiUserViewSet.as_view({'get': 'info'})),
] + router.urls


