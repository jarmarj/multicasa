from django.db import models

# Create your models here.

class Casa(models.Model):
    calle = models.CharField(max_length=50)
    colonia = models.CharField(max_length=50, default='')
    ciudad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cp = models.IntegerField()
    precio = models.FloatField()
    recamaras = models.IntegerField()
    banos = models.IntegerField()
    # imagen = models.ImageField(upload_to='casas', null=True)
    vendida = models.BooleanField(max_length=10, default=False)
    metros = models.FloatField(default=200.0)
    latitud = models.CharField(max_length=50, null=True)
    longitud = models.CharField(max_length=50, null=True)

    def __str__(self):
        return '%s, %s, %s, $%s, %s' % (self.calle, self.colonia, self.ciudad, self.precio, self.vendida)

class ImagenCasa(models.Model):
    imagen = models.ImageField(upload_to='casas')
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE, related_name='imagenes')

class ClienteCasa(models.Model):
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE, related_name='clientes')