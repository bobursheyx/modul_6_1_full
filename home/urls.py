from django.urls import path
from home .views import get_info, get_name, get_view

urlpatterns = [
    path('app_urls', get_info),
    path('app_names', get_name),
    path('app_views', get_view),
]