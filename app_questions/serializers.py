from dvizhenie.core.loading import get_model
from rest_framework import serializers

__all__ = [
    'QuestionSerializer',
    'AnswerSerializer',
]

Question = get_model('questions', 'Question')
Answer = get_model('questions', 'Answer')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
