from django.shortcuts import render
from promotions.models import Promotion

from rest_framework import viewsets
from promotions.serializers import PromotionSerializer

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer