from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('dojo_survey_app', views.index),
    path('result', views.summary),
]