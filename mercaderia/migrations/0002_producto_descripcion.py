# Generated by Django 4.1.3 on 2022-11-18 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercaderia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
