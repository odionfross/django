"""the_wall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include

urlpatterns = [
    path('', include('login_app.urls')),
    path('wall/', include('wall_app.urls'))
]

# This is the syntax if I want to route multiple apps from one file - the project level url.py

# from django.urls import path, include
# from login_app import views as login_views
# from wall_app import views as wall_views

# urlpatterns = [
#     path('', login_views.login_reg, name='login_reg'),
#     # path('success', login_views.success, name='create-user'),
#     path('wall', wall_views.wall, name='wall'),
#     # path('wall/success', wall_views.success, name='create-comment'),
# ]
