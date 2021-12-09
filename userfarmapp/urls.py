from django.urls import path
from .views import AccountListCreate,AccountListUpdateDelete,DeliverListCreate,DeliverListUpdateDelete,DeliveryListCreate,DeliveryListUpdateDelete
urlpatterns = [
    path('account/', AccountListCreate.as_view()), 
    path('account/<pk>/',AccountListUpdateDelete.as_view()), 
    path('deliver/',DeliverListCreate.as_view()), 
    path('deliver/<pk>/', DeliverListUpdateDelete.as_view()),
    path('delivery/',DeliveryListCreate.as_view()),
    path('delivery/<pk>/',DeliverListUpdateDelete.as_view()),

]
