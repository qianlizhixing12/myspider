from django.urls import path
from . import views

urlpatterns = [
    path('login.html', views.loginpage),
    path('index.html', views.indexpage),
    path('info.html', views.infopage),
    path('attr.html', views.attrpage),
    path('report.html', views.reportpage),
]