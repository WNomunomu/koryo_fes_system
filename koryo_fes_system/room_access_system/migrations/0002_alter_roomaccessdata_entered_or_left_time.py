# Generated by Django 3.2.12 on 2022-03-10 14:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('room_access_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomaccessdata',
            name='entered_or_left_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]