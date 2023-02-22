from rest_framework import serializers
from dvizhenie.core.loading import get_model


Project = get_model('projects', 'Project')
Partner = get_model('projects', 'Partner')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"
