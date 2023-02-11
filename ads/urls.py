from django.urls import path
from ads.views import root

urlpatterns = [
    path('', root),
]