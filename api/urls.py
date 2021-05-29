from django.urls import path,include
from . import views

urlpatterns = [
    path('get_richtunge_items', views.GetRichtungeItems.as_view()),
    path('get_richtunge_item', views.GetRichtungeItem.as_view()),

    path('get_table_items', views.GetTableItems.as_view()),
    path('get_table_item', views.GetTableItem.as_view()),



]
