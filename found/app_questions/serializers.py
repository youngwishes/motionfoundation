from dvizhenie.core.loading import get_model
from rest_framework import serializers

__all__ = [
    'QuestionSerializer',
]

Question = get_model('questions', 'Question')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
