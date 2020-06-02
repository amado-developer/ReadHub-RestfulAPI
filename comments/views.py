from django.shortcuts import render
from rest_framework import viewsets
from comments.models import Comment
from comments.serializers import CommentSerializer
from digital_books.models import Digital_Book
from rest_framework.decorators import action
from rest_framework.response import Response

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=False, url_path='get-comments', methods=['get'])
    def get_comments(self, request):
        book_id = request.query_params['book']
        comments = Comment.objects.filter(book=book_id)
        return Response(CommentSerializer(comments, many=True).data)