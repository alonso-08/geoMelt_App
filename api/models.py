from django.db import models


class Folder(models.Model):
    name = models.TextField(max_length=120, default='default')


class Linea(models.Model):
    name = models.TextField(max_length=120, default='default')


class Ramal(models.Model):
    name = models.TextField(max_length=120, default='default')


class Servicio(models.Model):
    name = models.TextField(max_length=120, default='default')


class Actualidad(models.Model):
    name = models.TextField(max_length=120, default='default')


class TipoObra(models.Model):
    name = models.TextField(max_length=120, default='default')


class KmlData(models.Model):
    name = models.TextField(max_length=120, default='default', null=True)
    folder_id = models.ForeignKey(Folder, on_delete=models.CASCADE)
    line_id = models.ForeignKey(Linea, on_delete=models.CASCADE)
    ramal_id = models.ForeignKey(Ramal, on_delete=models.CASCADE)
    servicio_id = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    actualidad_id = models.ForeignKey(Actualidad, on_delete=models.CASCADE)
    obra_id = models.ForeignKey(TipoObra, on_delete=models.CASCADE)
    placeName = models.TextField(max_length=120, default='default')
    placeDescription = models.TextField(max_length=120, default='default')
    lat = models.TextField(max_length=120, default='default')
    lon = models.TextField(max_length=120, default='default')
    nomAlt = models.TextField(max_length=120, default='default')
    obs = models.TextField(max_length=120, default='default')
    prev2019 = models.TextField(max_length=120, default='default')
    prev2023 = models.TextField(max_length=120, default='default')
    estado = models.TextField(max_length=120, default='default')
    progresiva = models.TextField(max_length=120, default='default')
    anoEstimadoDeObra = models.TextField(max_length=120, default='default')
    ultimaActualizacion = models.TextField(max_length=120, default='default')

