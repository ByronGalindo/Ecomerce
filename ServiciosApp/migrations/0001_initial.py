# Generated by Django 4.1 on 2023-07-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreServicio', models.CharField(max_length=50)),
                ('ContenidoServicio', models.CharField(max_length=100)),
                ('Imagen', models.ImageField(upload_to=None)),
                ('FechaCreacionServicio', models.DateTimeField(auto_now_add=True)),
                ('FechaActualizacionServicio', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
    ]