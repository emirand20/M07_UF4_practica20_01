# Generated by Django 4.1.6 on 2023-05-03 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='fecha_actualizacion',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='fecha_creacion',
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=64),
        ),
    ]
