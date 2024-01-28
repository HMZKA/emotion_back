from rest_framework import serializers

from job.models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ("title", "description", "company_id")

    def create(self, validated_data):
        
        return Job.objects.create(**validated_data)
