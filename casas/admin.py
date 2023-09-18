from django.contrib import admin
from casas.models import Casa, ImagenCasa, ClienteCasa

# Register your models here.

class CleinteCasaAdmin(admin.TabularInline):
    model = ClienteCasa

class ImagenCasaAdmin(admin.TabularInline):
    model = ImagenCasa


class CasaAdmin(admin.ModelAdmin):
    list_display = ('colonia', 'vendida', 'calle', 'ciudad', 'precio', 'id')
    list_filter = ('colonia', 'ciudad', 'vendida','recamaras','banos')
    inlines = [
        ImagenCasaAdmin,
        CleinteCasaAdmin
    ]

admin.site.register(Casa, CasaAdmin)
