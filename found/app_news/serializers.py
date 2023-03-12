from rest_framework import serializers
from dvizhenie.core.loading import get_model


News = get_model('news', 'News')


class NewsSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')
    updated_at = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')

    class Meta:
        model = News
        fields = "__all__"


