from rest_framework import serializers
from dvizhenie.core.loading import get_model


FundEvent = get_model('events', 'FundEvent')
Address = get_model('events', 'Address')


class EventSerializer(serializers.ModelSerializer):
    start_timestamp = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')
    end_timestamp = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')

    class Meta:
        model = FundEvent
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
