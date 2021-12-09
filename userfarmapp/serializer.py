from rest_framework import serializers
from .models import Account, Deliver, Delivery

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class DeliverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliver
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    deliver =DeliverSerializer
    class Meta:
        model = Delivery
        fields = '__all__'

