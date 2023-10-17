from rest_framework import serializers
from students.models import Student
from rest_framework.validators import UniqueValidator
from tracks.models import Track
from tracks.api.serializers import  TrackSerializer
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) # cannot be modified
    name = serializers.CharField(max_length=100)
    email= serializers.EmailField(validators=[UniqueValidator(queryset=Student.objects.all())])
    grade = serializers.IntegerField(default=0)
    image = serializers.ImageField( required=False)  # to be solved
    # when request data for read ---> image.url
    track = TrackSerializer(read_only=True)
    # track = serializers.StringRelatedField(read_only=True)
    track_id = serializers.IntegerField(write_only=True, required=False)
    track_name = serializers.CharField(source="track", read_only=True)
    track_logo = serializers.ImageField(source='track.logo', read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


    def create(self, validated_data):
        print(validated_data)
        print('here in create')
        return Student.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.email = validated_data.get('email')
        instance.grade = validated_data.get('grade')
        instance.image = validated_data.get('image')
        instance.save()
        return  instance
