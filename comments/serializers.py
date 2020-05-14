from rest_framework import serializers
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    book = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = (
            'id',
            'type',
            'message',
            'date',
            'user',
            'book',

        )

    def get_user(self,object):
        return ''
    def get_book(self,object):
        return ''
