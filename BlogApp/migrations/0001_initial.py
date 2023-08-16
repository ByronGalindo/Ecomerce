# Generated by Django 4.1 on 2023-07-16 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreCategoria', models.CharField(max_length=50, verbose_name='Categoria')),
                ('FechaCreacionCategoria', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('FechaActualizacionCategoria', models.DateTimeField(auto_now_add=True, verbose_name='Actualizado')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombrePost', models.CharField(max_length=50, verbose_name='Post')),
                ('ContenidoPost', models.CharField(max_length=100, verbose_name='Contenido')),
                ('Imagen', models.ImageField(blank=True, null=True, upload_to='BlogApp', verbose_name='Imagen')),
                ('FechaCreacionPost', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('FechaActualizacionPost', models.DateTimeField(auto_now_add=True, verbose_name='Actualizado')),
                ('AutorPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Categorias', models.ManyToManyField(to='BlogApp.categorias')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]