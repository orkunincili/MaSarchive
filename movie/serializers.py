
from rest_framework import serializers


class movieSerializer(serializers.Serializer):
       
    movie_name = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=50)
    poster = serializers.CharField(max_length=200)
    movie_rate= serializers.CharField(max_length=7)
    imdb_page=serializers.CharField(max_length=100)
    duration=serializers.CharField(max_length=15)
