# Generated by Django 3.2.4 on 2021-07-05 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_description_categoria_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='productos'),
        ),
    ]
