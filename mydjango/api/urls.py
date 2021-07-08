from django.urls import path
from . import views

urlpatterns = [
    path('custom/login.do', views.custom_logindo),
    path('custom/create.do', views.custom_createdo),
    path('custom/logout.do', views.custom_logoutdo),
    path('custom/get.do', views.custom_getdo),
    path('custom/edit.do', views.custom_editdo),
    path('custom/attr/get.do', views.custom_attr_getdo),
    path('custom/attr/edit.do', views.custom_attr_editdo),
    path('gaokao/scoollist/get.do', views.gaokao_scoollist_getdo),
]