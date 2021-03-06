# Generated by Django 3.0.1 on 2019-12-24 02:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inv', '0004_um'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('Codigo', models.CharField(max_length=20, unique=True)),
                ('Codigo_Barra', models.CharField(max_length=50)),
                ('Descripcion', models.CharField(max_length=200)),
                ('Precio', models.FloatField(default=0)),
                ('Existencia', models.IntegerField(default=0)),
                ('Ultima_Compra', models.DateField(blank=True, null=True)),
                ('objMarca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.Marca')),
                ('objSubcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.Subcategoria')),
                ('objUM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.UM')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Unidades de Medida',
                'unique_together': {('Codigo', 'Codigo_Barra')},
            },
        ),
    ]
