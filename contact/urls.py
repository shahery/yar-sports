# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact_view')
]
