from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from equipmentloans.models import EquipmentLoan
from equipmentloans.serializers import EquipmentLoanSerializer
from users.models import User
from equipments.models import Equipment
from rest_framework.response import Response

class EquipmentLoanViewSet(viewsets.ModelViewSet):
    queryset = EquipmentLoan.objects.all()
    serializer_class = EquipmentLoanSerializer


    @action(detail=False, url_path='get-loans', methods=['get'])
    def get_equipment_loans(self, request):
        user_id= request.query_params['user']
        user = User.objects.get(pk=user_id)
        equipment_loan = EquipmentLoan.objects.filter(user=user)

        return Response(EquipmentLoanSerializer(equipment_loan, many=True).data)



    @action(detail=False, url_path='return-equipment', methods=['patch'])
    def return_equipment(self, request):

       # user_id= request.query_params['user']
        #user = User.objects.get(pk=user_id)

        equipment_id = request.query_params['equipment']
        print(equipment_id)
        equipment_loan_object = EquipmentLoan.objects.filter(pk=equipment_id).values()
        id = list(equipment_loan_object)[0]['equipment_id']

        print(id)
        equipment = Equipment.objects.get(pk=id)
        
    
        equipment.quantity = equipment.quantity + 1
       
        equipment_loan = EquipmentLoan.objects.filter(pk=equipment_id)
        equipment.save()
        equipment_loan.delete()

        return Response({'Deleted': 'Equipment Deleted Succesfully'})



    @action(detail=False, url_path='pick-equipment', methods=['post'])
    def pick_equipment(self, request):
        print(request.data)
        equipment_id = request.data['equipment']
        user_id= request.data['user']
        devoldate = request.data['devolution_date']
        user = User.objects.get(pk=user_id)
        for id in equipment_id:
            equipment = Equipment.objects.get(pk=id)
            equipment.quantity = equipment.quantity - 1
            equipment_loan = EquipmentLoan()
            print(equipment.quantity)
            if equipment.quantity < 0:
                return Response({'Sorry':'No available units'})
            else:
                equipment.save()
                equipment_loan.equipment = equipment
                equipment_loan.user = user
                equipment_loan.devolution_date = devoldate
                equipment_loan.fee = 0
                equipment_loan.save()
        return Response({'created': 'Book loan created Succesfully'})



        
 



        
        




