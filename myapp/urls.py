from django.urls import path

from myapp.views import get_join, get_raw_query

myapp_url = [
  path("join/", get_join),
  path("raw/", get_raw_query)
]
