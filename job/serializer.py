from rest_framework import serializers

from job.models import Job
from user.serializer import UserSerializer


class JobSerializer(serializers.ModelSerializer):
    applicants = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Job
        fields = ("title", "description", "company_id","applicants")

    def create(self, validated_data):
        
        return Job.objects.create(**validated_data)
