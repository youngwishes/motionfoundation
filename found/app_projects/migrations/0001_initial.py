# Generated::w by Django 4.1.6 on 2023-02-24 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, verbose_name='name')),
                ('logo', models.ImageField(upload_to='partners', verbose_name='logo')),
            ],
            options={
                'verbose_name': 'partner',
                'verbose_name_plural': 'partners',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=128, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('start_timestamp', models.DateTimeField(verbose_name='start timestamp')),
                ('end_timestamp', models.DateTimeField(verbose_name='end timestamp')),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
                'ordering': ('start_timestamp',),
            },
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=256, verbose_name='тип проекта')),
            ],
            options={
                'verbose_name': 'тип проекта',
                'verbose_name_plural': 'типы проектов',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ProjectPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото проекта')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='projects.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.projecttype', verbose_name='тип проекта'),
        ),
    ]
