from django.urls import path, include
from . import views

urlpatterns = [
    path('colori/', views.index, name='index'),
    path('colori/<int:color_id>', views.color_details, name="color_details")
]