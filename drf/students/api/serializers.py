from rest_framework import serializers



class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) # cannot be modified
    name = serializers.CharField(max_length=100)
    email= serializers.EmailField()
    grade = serializers.IntegerField(default=0)
    image = serializers.ImageField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

