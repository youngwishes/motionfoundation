from rest_framework import serializers
from dvizhenie.core.loading import get_model


Activity = get_model('activities', 'Activity')
ActivityType = get_model('activities', 'ActivityType')


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"


class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = "__all__"
