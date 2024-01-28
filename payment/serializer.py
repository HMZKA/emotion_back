from rest_framework import serializers

from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

    def create(self, validted_data):
        return Payment.objects.create(**validted_data)
    
