# Generated by Django 2.1.2 on 2018-10-23 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_auto_20181023_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rostros',
            name='cantidad_pix',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rostros',
            name='intensidad_pix',
            field=models.IntegerField(),
        ),
    ]
