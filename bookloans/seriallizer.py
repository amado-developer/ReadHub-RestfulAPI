from .models import BookLoan
from rest_framework import serializers

class BookLoanSerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField()
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
    def get_book(self, obj):
        return{
            "id": obj.book.id,
            "name": obj.book.name,
            "author": obj.book.author.pseudonym,
            "publisher": obj.book.publisher,
            "edition": obj.book.edition,
            "release_date": obj.book.release_date,
            "isbn": obj.book.isbn,
            "cover": obj.book.cover.url,
        }