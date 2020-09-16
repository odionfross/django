from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<int:page_id>', views.show),
    path('<int:page_id>/edit', views.edit),
    path('<int:page_id>/delete', views.destroy),
]