# Generated by Django 2.1.1 on 2018-10-05 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='friend',
            name='gender',
            field=models.BooleanField(),
        ),
    ]
