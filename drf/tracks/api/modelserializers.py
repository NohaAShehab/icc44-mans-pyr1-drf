from rest_framework import serializers

from tracks.models import Track


class TrackModelSerializer(serializers.ModelSerializer):
    students = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Track
        fields = '__all__'


    def validate_name(self,name):
        if name.lower()=='iti':
            raise serializers.ValidationError('Track name should not be iti')
        return name
