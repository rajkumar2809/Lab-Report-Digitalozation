# Generated by Django 2.0.5 on 2020-02-15 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myfile',
            name='size',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='myfile',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
