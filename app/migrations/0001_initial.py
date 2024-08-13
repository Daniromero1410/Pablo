# Generated by Django 5.1 on 2024-08-12 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gaia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('convocatoria', models.CharField(blank=True, max_length=255, null=True)),
                ('codigo_proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('nombre_proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('fecha_finalizacion', models.DateField(blank=True, null=True)),
                ('sede', models.CharField(blank=True, max_length=255, null=True)),
                ('grupo_investigacion', models.CharField(blank=True, max_length=255, null=True)),
                ('programas_academicos', models.CharField(blank=True, max_length=255, null=True)),
                ('investigador_principal', models.CharField(blank=True, max_length=255, null=True)),
                ('coinvestigadores', models.TextField(blank=True, null=True)),
                ('productos_comprometidos', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Gaia',
            },
        ),
        migrations.CreateModel(
            name='Gnt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('convocatoria', models.CharField(blank=True, max_length=255, null=True)),
                ('codigo_proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('nombre_proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('fecha_finalizacion', models.DateField(blank=True, null=True)),
                ('sede', models.CharField(blank=True, max_length=255, null=True)),
                ('grupo_investigacion', models.CharField(blank=True, max_length=255, null=True)),
                ('programas_academicos', models.CharField(blank=True, max_length=255, null=True)),
                ('investigador_principal', models.CharField(blank=True, max_length=255, null=True)),
                ('coinvestigadores', models.TextField(blank=True, null=True)),
                ('productos_comprometidos', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingenieria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('convocatoria', models.CharField(blank=True, max_length=255, null=True)),
                ('codigo_proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('nombre_proyecto', models.CharField(blank=True, max_length=255, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('fecha_finalizacion', models.DateField(blank=True, null=True)),
                ('sede', models.CharField(blank=True, max_length=255, null=True)),
                ('grupo_investigacion', models.CharField(blank=True, max_length=255, null=True)),
                ('programas_academicos', models.CharField(blank=True, max_length=255, null=True)),
                ('investigador_principal', models.CharField(blank=True, max_length=255, null=True)),
                ('coinvestigadores', models.TextField(blank=True, null=True)),
                ('productos_comprometidos', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Ingenieria',
            },
        ),
    ]
