from django.urls import path
from bbs.views import home_view

urlpatterns = [
    path('', home_view, name='bbs_home'),
]