from django.urls import path
from . import views

app_name = 'vehicle'

urlpatterns = [
    path('', views.get_48_hours, name='vehicle_data'),
]
