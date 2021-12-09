from django.shortcuts import render
from rest_framework import generics, authentication, permissions

from .models import Account, Deliver,Delivery
from .serializer import AccountSerializer,DeliverSerializer, DeliverySerializer

# # Create your views here.

class AccountListCreate(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class AccountListUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class DeliverListCreate(generics.ListCreateAPIView):
    queryset = Deliver.objects.all()
    serializer_class = DeliverSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class DeliverListUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deliver.objects.all()
    serializer_class = DeliverSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class DeliveryListCreate(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class DeliveryListUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

