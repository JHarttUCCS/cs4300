from django.urls import path, include
from rest_framework import routers

from . import views


# create router and register the viewsets
router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet, basename='movie')


urlpatterns = [
    path('api/', include(router.urls)),
]
