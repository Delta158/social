# Generated by Django 4.0.2 on 2022-03-01 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='core/event/')),
                ('datetime', models.DateTimeField(blank=True)),
                ('street', models.CharField(blank=True, max_length=50)),
                ('area', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('desc', models.TextField(max_length=400)),
                ('ticket', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('discord', models.URLField(blank=True)),
                ('attendance', models.IntegerField(default=0)),
            ],
        ),
    ]
