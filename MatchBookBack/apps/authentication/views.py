from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.files.uploadedfile import InMemoryUploadedFile
import requests
import os

from .models import User, UserProfileImage
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly

IMGUR_CLIENT_ID = os.environ.get('IMGUR_CLIENT_ID')
IMGUR_API_URL = os.environ.get('IMGUR_API_URL')

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]

class UserImageUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user

        image_request: InMemoryUploadedFile = request.data.get('image')
  
        if type(image_request) != InMemoryUploadedFile:
            return Response({'error': 'Invalid image'}, status=400)

        image = image_request.file.read()

        imgur_response = requests.post(
            f'{IMGUR_API_URL}/image',
            headers={
                'Authorization': f'Client-ID {IMGUR_CLIENT_ID}'
            },
            data={
                'image': image
            }
        )

        if imgur_response.status_code >= 400:
            return Response({'error': 'Image upload failed'}, status=400)

        imgur_response_data = imgur_response.json()

        user.profile_image = UserProfileImage.objects.create(
            url=imgur_response_data.get('data').get('link'),
            delete_hash=imgur_response_data.get('data').get('deletehash')
        )

        user.save()

        return Response({'message': 'Image uploaded successfully'}, status=200)



