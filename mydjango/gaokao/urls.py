from django.urls import path
from . import views

urlpatterns = [
    path('schooltop.html', views.schooltop),
    path('schoollist.html', views.schoollist),
]