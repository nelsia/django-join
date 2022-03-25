from django.urls import path, include
from rest_framework.routers import DefaultRouter

from myapp.views import get_join, get_raw_query, RecordViewSet


router = DefaultRouter()
router.register("record", RecordViewSet, basename="record")

myapp_url = [
  path("join/", get_join),
  path("raw/", get_raw_query),
  path("", include(router.urls))
]
