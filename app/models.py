from django.db import models

# Create your models here.
class Ingenieria(models.Model):
    convocatoria = models.CharField(max_length=255, blank=True, null=True)
    codigo_proyecto = models.CharField(max_length=255, blank=True, null=True)
    nombre_proyecto = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_finalizacion = models.DateField(blank=True, null=True)
    sede = models.CharField(max_length=255, blank=True, null=True)
    grupo_investigacion = models.CharField(max_length=255, blank=True, null=True)
    programas_academicos = models.CharField(max_length=255, blank=True, null=True)
    investigador_principal = models.CharField(max_length=255, blank=True, null=True)
    coinvestigadores = models.TextField(blank=True, null=True)
    productos_comprometidos = models.TextField(blank=True, null=True)

    class Meta:
        db_table='Ingenieria'

class Gaia(models.Model):
    convocatoria = models.CharField(max_length=255, blank=True, null=True)
    codigo_proyecto = models.CharField(max_length=255, blank=True, null=True)
    nombre_proyecto = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_finalizacion = models.DateField(blank=True, null=True)
    sede = models.CharField(max_length=255, blank=True, null=True)
    grupo_investigacion = models.CharField(max_length=255, blank=True, null=True)
    programas_academicos = models.CharField(max_length=255, blank=True, null=True)
    investigador_principal = models.CharField(max_length=255, blank=True, null=True)
    coinvestigadores = models.TextField(blank=True, null=True)
    productos_comprometidos = models.TextField(blank=True, null=True)

    class Meta:
        db_table='Gaia'
    
class Gnt(models.Model):
    convocatoria = models.CharField(max_length=255, blank=True, null=True)
    codigo_proyecto = models.CharField(max_length=255, blank=True, null=True)
    nombre_proyecto = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_finalizacion = models.DateField(blank=True, null=True)
    sede = models.CharField(max_length=255, blank=True, null=True)
    grupo_investigacion = models.CharField(max_length=255, blank=True, null=True)
    programas_academicos = models.CharField(max_length=255, blank=True, null=True)
    investigador_principal = models.CharField(max_length=255, blank=True, null=True)
    coinvestigadores = models.TextField(blank=True, null=True)
    productos_comprometidos = models.TextField(blank=True, null=True)

    class Meta: 
        db_table='Gnt'
