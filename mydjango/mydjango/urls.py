"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('custom/', include('custom.urls')),
    path('gaokao/', include('gaokao.urls')),
    path('', RedirectView.as_view(url='/custom/index.html', permanent=True)),
]

handler500 = 'custom.views.server_error'
# handler400 = 'custom.views.bad_request'
handler403 = 'custom.views.forbidden'
handler404 = 'custom.views.page_not_found'
