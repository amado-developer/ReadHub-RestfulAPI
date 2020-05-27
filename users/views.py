from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view,  permission_classes, parser_classes
from .serializers import UserSerializer
from rest_framework import permissions
from .models import User
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser, JSONParser
from django.core.files.base import ContentFile
from permissions.services import APIPermissionClassFactory

def isLogged(user, obj, request):
    # print(obj.email)
    return user.email == obj.email
    # return True

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (
        APIPermissionClassFactory(
            name='UserPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': False,
                },
                'instance': {
                    'retrieve': isLogged,
                    'destroy': False,
                    'update': True,
                }
            }
        ),
    )
# import base64
# @api_view(['POST'])
# @permission_classes([permissions.AllowAny])
# def registration_view(request):
#     if(request.method == 'POST'):
#         serializer = UserSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             user = serializer.save()
#             data['response'] = "Succesfully registered!"
#         else: 
#             data = serializer.errors
#         return Response(data)

# @api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated])
# def users_view(request):
#     if(request.method == 'GET'):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
    
#     return Response(serializer.data)

# @api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated])
# def user_view(request, pk):
#     try:

#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

# import base64
# @api_view(['PATCH', 'PUT'])
# @permission_classes([permissions.IsAuthenticated])
# @parser_classes([ JSONParser,FormParser, MultiPartParser])
# def upload_profile_picture(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     profile_picture = request.data['profile_picture']
#     user.profile_picture = profile_picture
#     user.save()
#     # print(profile_picture)
#     return Response(str(profile_picture))

