from django.urls import path
from items import views

urlpatterns = [
    path('item/<int:id>/', views.item_detail, name='item_detail')
]
