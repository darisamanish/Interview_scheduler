# Generated by Django 3.0.5 on 2020-10-24 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting_time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('startTime', models.CharField(max_length=5)),
                ('endTime', models.CharField(max_length=5)),
            ],
        ),
    ]
