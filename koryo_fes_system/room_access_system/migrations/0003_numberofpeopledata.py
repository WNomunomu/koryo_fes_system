# Generated by Django 3.1.5 on 2022-05-22 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_access_system', '0002_alter_roomaccessdata_entered_or_left_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumberOfPeopleData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=20)),
                ('number_of_people', models.BigIntegerField(default=0)),
            ],
        ),
    ]