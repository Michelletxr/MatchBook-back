from django.urls import path
from .views import MessageCreateView, RoomListView, RoomRetrieveView

urlpatterns = [
    path('messages/', MessageCreateView.as_view(), name='messages'),
    path('rooms/', RoomListView.as_view(), name='rooms'),
    path('rooms/<uuid:pk>/', RoomRetrieveView.as_view(), name='room'),
]
