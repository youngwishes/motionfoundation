# Generated by Django 4.1.6 on 2023-02-05 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_partner_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectphoto',
            name='photo',
            field=models.ImageField(default=1, upload_to='', verbose_name='Фото проекта'),
            preserve_default=False,
        ),
    ]