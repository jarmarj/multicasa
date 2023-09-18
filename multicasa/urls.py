"""multicasa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from casas.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('multicasa/', include('casas.urls'))
    # path('', inicio, name='inicio'),
    # path('company/', company),
    # path('servicios/', servicios),
    # path('requisitos/', requisitos),
    # path('contactos/', contactos),
    # path('results/', results),
    # path('details/<str:id>', details),
    # path('multicasa_pdf/<str:id>', multicasa_pdf, name='multicasa_pdf'),
    # path('asesoria/', asesoria),
    # path('dashboard/', dashboard),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
