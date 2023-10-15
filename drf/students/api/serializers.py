from rest_framework import serializers
from students.models import Student
from rest_framework.validators import UniqueValidator

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) # cannot be modified
    name = serializers.CharField(max_length=100)
    email= serializers.EmailField(validators=[UniqueValidator(queryset=Student.objects.all())])
    grade = serializers.IntegerField(default=0)
    image = serializers.ImageField(allow_null=True, allow_empty_file=True)  # to be solved
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


    def create(self, validated_data):
        print(validated_data)
        print('here in create')
        return Student.objects.create(**validated_data)



