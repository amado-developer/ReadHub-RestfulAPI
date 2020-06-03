from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from studyclassrooms_reservations.models import StudyClassrooms_Reservation
from studyclassrooms_reservations.serializers import StudyClassroom_ReservationSerializer
from rest_framework.response import Response
from users.models import User
from studyclassrooms.models import StudyClassrooom


class StudyClassrooms_ReservationViewSet(viewsets.ModelViewSet):
    queryset = StudyClassrooms_Reservation.objects.all()
    serializer_class = StudyClassroom_ReservationSerializer

    @action(detail=False, url_path='return-classroom', methods=['patch'])
    def return_class(self, request):
        user_id= request.query_params['user']
        user = User.objects.get(pk=user_id)

        class_id = request.query_params['studyclassroom']
        classroom = StudyClassrooom.objects.get(pk=class_id)
    
        classroom.quantity = classroom.quantity + 1
       
        class_loan = StudyClassrooms_Reservation.objects.filter(user=user, studyclassroom=studyclassroom)
        classroom.save()
        class_loan.delete()

        return Response({'Deleted': 'studyclassroom Deleted Succesfully'})



    @action(detail=False, url_path='loan-classroom', methods=['post'])
    def loan_class(self, request):

        class_id = request.data['studyclassroom']
        user_id= request.data['user']
        devoldate = request.data['devolution_date']
        
        user = User.objects.get(pk=user_id)
        classroom = StudyClassrooom.objects.get(pk=class_id)
        

        classroom.quantity = classroom.quantity - 1
        class_loan = StudyClassrooms_Reservation()
    
        if classroom.quantity < 0:
             return Response({'sorry':'No available units'})
        else:
            classroom.save()
            class_loan.equipment = classroom
            class_loan.user = user
            class_loan.devolution_date = devoldate
            class_loan.fee = 0
            class_loan.save()
            return Response({'created': 'Equipment loan created Succesfully'})

