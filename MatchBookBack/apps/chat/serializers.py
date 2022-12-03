from django.dispatch import receiver
from rest_framework import serializers
from django.db.models import Q

from .models import Message, Room
from authentication.serializers import UserSerializer

class MessageSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    to = serializers.UUIDField(required=True, write_only=True)
    author = UserSerializer(read_only=True)
    content = serializers.CharField(required=True)

    def create(self, validated_data):
        sender_id = self.context['request'].user.id
        receiver_id = validated_data.get('to')

        
        room = Room.objects.filter(users__in=[sender_id, receiver_id]).first()
        
        if not room:
            room = Room.objects.create()
            room.users.add(self.context['request'].user)
            room.users.add(validated_data['to'])

        message = Message.objects.create(
            room=room,
            author_id=self.context['request'].user.id,
            content=validated_data.get('content'),
        )

        return message

    class Meta:
        model = Message
        fields = '__all__'

class RoomListSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    users = UserSerializer(read_only=True, many=True)

    def list(self, request):
        rooms = Room.objects.values(
            'id',
            'users'
        ).filter(
            users__in=[request.user.id]
        )

        return rooms

    class Meta:
        model = Room
        fields = ('id', 'users')

class RoomSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    users = UserSerializer(read_only=True, many=True)
    messages = MessageSerializer(many=True, read_only=True)

    def retrieve(self, request, pk=None):
        print('@'*2000)
        room = Room.objects.filter(
            Q(users__id=request.user.id) & Q(id=pk)
        ).first()

        return room

    class Meta:
        model = Room
        fields = ('id', 'users', 'messages')