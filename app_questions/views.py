from rest_framework import viewsets
from dvizhenie.core.loading import get_model
from .serializers import *
from rest_framework import permissions


Question = get_model('questions', 'Question')
Answer = get_model('questions', 'Answer')


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().select_related('question')
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
