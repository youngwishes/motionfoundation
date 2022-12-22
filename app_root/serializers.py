from rest_framework import serializers
from dvizhenie.core.loading import get_model

__all__ = [
    'AboutTheFundSerializer',
    'ContactsSerializer',
    'FileSerializer',
]

AboutTheFund = get_model('root', 'AboutTheFund')
Contacts = get_model('root', 'Contacts')
File = get_model('root', 'File')


class AboutTheFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutTheFund
        fields = "__all__"


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
