from django.urls import path
from . import views

urlpatterns = [
	path('', views.index), # redirects to shows
    path('shows', views.shows), # renders all the shows
    path('shows/new', views.new_show), # renders a form to add a show
    path('shows/create', views.create_show), # creates a new show and redirects
    path('shows/<int:id>', views.view_shows), # renders a single show route
    path('shows/<int:id>/edit', views.edit_show), # renders page to edit show
    path('shows/<int:id>/update', views.update_show), # update shows info
    path('shows/<int:id>/destroy', views.delete_show)
]