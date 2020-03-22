# Generated by Django 3.0.4 on 2020-03-21 22:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='admins',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='CourseMaintainer',
        ),
    ]
