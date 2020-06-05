from rest_framework import viewsets
from .models import DigitalBookPDF
from .serializers import DigitalBookPDFSerializer
from rest_framework.decorators import action
from users.models import User
from users.serializers import UserSerializer
from digital_books.models import Digital_Book
from rest_framework.response import Response
from adquisitions.models import Collection
from adquisitions.serializers import CollectionSerializer

from permissions.services import APIPermissionClassFactory

def is_admin(user, request):
    return user.is_admin == True

def is_logged(user, obj, request):
    return user.email == obj.email

class DigitalBookPDFViewSet(viewsets.ModelViewSet):
    queryset = DigitalBookPDF.objects.all()
    serializer_class = DigitalBookPDFSerializer

    permission_classes = (
        APIPermissionClassFactory(
            name='UserPermission',
            permission_configuration={
                'base': {
                    'create': is_admin,
                    'list': True,
                },
                'instance': {
                    'retrieve': is_logged,
                    'destroy': False,
                    'update': False,
                    'get_pdf': is_logged,
                }
            }
        ),
    )

    @action(detail=False, url_path='get-pdf', methods=['get'])
    def get_pdf(self, request):
        user_id = request.query_params['user']
        user = User.objects.get(pk=user_id)
        collection = Collection.objects.filter(user=user)
        pdf = []
        for book in collection:
             try:
                 digitalBookPdf = DigitalBookPDF.objects.get(book=book.book)
                 pdf.append(DigitalBookPDFSerializer(digitalBookPdf).data)
           
             except DigitalBookPDF.DoesNotExist:
                pass
       
        return Response(pdf)
        #api/v1/digital-books-pdf/get-pdf/?user=#

