# Generated by Django 4.2 on 2023-04-19 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='position',
            field=models.IntegerField(null=True, verbose_name='Позиция'),
        ),
    ]
