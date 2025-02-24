from django.urls import path
from items import views

urlpatterns = [
    path('item/<int:id>/', views.item_detail, name='item_detail'),
    path('buy/<int:id>/', views.create_session, name='item_buy'),
    path('order/<int:id>/', views.create_session_order, name='order_detail'),
]
