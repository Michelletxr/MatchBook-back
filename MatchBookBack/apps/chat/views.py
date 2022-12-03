from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import MessageSerializer, RoomListSerializer, RoomSerializer
from .models import Message, Room
from .permissions import IsUserInRoom

class MessageCreateView(CreateAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    permission_classes = (IsAuthenticated,)

class RoomRetrieveView(RetrieveAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = (IsAuthenticated, IsUserInRoom)

class RoomListView(ListAPIView):
    serializer_class = RoomListSerializer
    queryset = Room.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(users__in=[self.request.user.id])
