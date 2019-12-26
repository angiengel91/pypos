# Generated by Django 3.0.1 on 2019-12-24 03:18

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
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('Descripcion', models.CharField(max_length=100, unique=True)),
                ('Direccion', models.CharField(blank=True, max_length=250, null=True)),
                ('Contacto', models.CharField(max_length=100)),
                ('Telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('Email', models.CharField(blank=True, max_length=250, null=True)),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
            },
        ),
    ]
