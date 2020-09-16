from django.urls import path
from . import views

urlpatterns = [
	path('', views.index), # renders homepage
    path('create', views.create), # add new course
    path('courses/destroy/<int:id>', views.single_course), # renders page to delete course
    path('delete/<int:id>', views.delete_course) # delete the single course
]