from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name='home'),
    path('company/', company, name='company'),
    path('servicios/', servicios, name='services'),
    path('requisitos/', requisitos,name='requisites'),
    path('contactos/', contactos, name='contacts'),
    path('results/', results, name='results'),
    path('details/<str:id>/', details, name='details'),
    path('multicasa_pdf/<str:id>/', multicasa_pdf, name='multicasa_pdf'),
    path('help/', help, name='help'),
    path('dashboard/', dashboard, name='dashboard')
]
