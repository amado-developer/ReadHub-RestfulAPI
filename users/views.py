from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,  permission_classes, parser_classes
from .serializers import RegistrationSerializer
from rest_framework import permissions
from .models import User
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser, JSONParser

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def registration_view(request):
    if(request.method == 'POST'):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Succesfully registered!"
        else: 
            data = serializer.errors
        return Response(data)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def users_view(request):
    if(request.method == 'GET'):
        users = User.objects.all()
        serializer = RegistrationSerializer(users, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def user_view(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegistrationSerializer(user)
        return Response(serializer.data)


@api_view(['PATCH', 'PUT'])
@permission_classes([permissions.AllowAny])
@parser_classes([ JSONParser,FormParser, MultiPartParser])
def upload_profile_picture(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    profile_picture = request.data['profile_picture']
    user.profile_picture = profile_picture
    user.save()
    print(profile_picture)
    return Response(str(profile_picture))
