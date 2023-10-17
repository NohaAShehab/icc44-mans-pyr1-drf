
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from tracks.models import  Track

class TrackSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=Track.get_all_objects())])
    description = serializers.CharField(max_length=200, required=False)
    logo  = serializers.ImageField(required=False)
    students = serializers.StringRelatedField(many=True, read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)




    def create(self, validated_data):
        return Track.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.logo = validated_data['logo']
        instance.save()
        return instance
