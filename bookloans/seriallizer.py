from .models import BookLoan
from rest_framework import serializers

class BookLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLoan
        fields = (
            'id',
            'user',
            'book',
            'loan_date',
            'devolution_date',
            'fee',
        )