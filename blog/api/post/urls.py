from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'',PostViewSet)


urlpatterns = [
    path('',include(router.urls))
]
