from .models import BookLoan
from .seriallizer import BookLoanSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from books.models import Book
from users.models import User
from rest_framework.response import Response
class BookLoanViewSet(viewsets.ModelViewSet):
    queryset = BookLoan.objects.all()
    serializer_class = BookLoanSerializer

    @action(detail=False, url_path='return-book', methods=['patch'])
    def return_book(self, request):
        book_id = request.query_params['book']
        user_id= request.query_params['user']
        book = Book.objects.get(pk=book_id)
        user = User.objects.get(pk=user_id)
        book_loan = BookLoan.objects.filter(user=user, book=book)
        book_loan.delete()
        return Response({'Deleted': 'Book Deleted Succesfully'})
    
    @action(detail=False, url_path='loan-book', methods=['post'])
    def loan_book(self, request):

        book_id = request.data['book']
        user_id= request.data['user']
        devoldate = request.data['devolution_date']
        
        user = User.objects.get(pk=user_id)
        book = Book.objects.get(pk=book_id)
        

        book.quantity = book.quantity - 1
        book_loan = BookLoan()
    
        if book.quantity < 0:
             return Response({'sorry':'No available units'})
        else:
            book.save()
            book_loan.book = book
            book_loan.user = user
            book_loan.devolution_date = devoldate
            book_loan.fee = 0
            book_loan.save()
            return Response({'created': 'Book loan created Succesfully'})

        


        

    
