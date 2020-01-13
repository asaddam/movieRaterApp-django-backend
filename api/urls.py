#1
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import MovieViewSet, RatingViewSet, UserViewSet #8 15userviewset

router = routers.DefaultRouter()
router.register('movies', MovieViewSet) #8
router.register('ratings', RatingViewSet) #8
router.register('users', UserViewSet) #15 for register and login

urlpatterns = [
    path('', include(router.urls)),
]
