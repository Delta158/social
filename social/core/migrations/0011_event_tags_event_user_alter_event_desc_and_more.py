# Generated by Django 4.0.2 on 2022-03-31 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0010_event_user_alter_event_datetime_alter_event_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='desc',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
