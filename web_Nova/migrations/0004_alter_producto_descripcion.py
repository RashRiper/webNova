# Generated by Django 5.1.3 on 2024-11-19 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_Nova', '0003_producto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, default='Sin descripción', null=True),
        ),
    ]
