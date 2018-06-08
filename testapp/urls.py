from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us, name='contact_us'),
    path('', views.register, name='register'),
    path('', views.add_feature, name='add_feature'),
]