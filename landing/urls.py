from django.urls import path
from .views import PizzaOrderView

urlpatterns = [
    path('', PizzaOrderView.as_view(), name='order'),
]