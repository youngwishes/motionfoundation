from rest_framework import serializers
from dvizhenie.core.loading import get_model


FundEvent = get_model('events', 'FundEvent')
Address = get_model('events', 'Address')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundEvent
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
