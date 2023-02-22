from rest_framework import serializers
from dvizhenie.core.loading import get_model


News = get_model('news', 'News')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
