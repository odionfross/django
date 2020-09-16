from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall),
    path('logout', views.logout),
    path('<int:mess_id>/comment', views.comment),
    path('delete_message/<int:mess_id>', views.delete_message),
]