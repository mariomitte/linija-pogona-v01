from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter
from api.views import OperaterViewSet

router = DefaultRouter()
router.register(prefix='operater', viewset=OperaterViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
