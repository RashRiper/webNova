# Generated by Django 5.1.3 on 2024-11-19 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_Nova', '0002_producto_almacenamiento_fuente_memoriaram_pantalla_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(default='Sin descripcion'),
            preserve_default=False,
        ),
    ]
