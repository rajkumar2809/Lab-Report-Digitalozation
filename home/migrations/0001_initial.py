# Generated by Django 2.0.5 on 2020-02-15 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myuser',
            fields=[
                ('Username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Email', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=20)),
                ('FirstName', models.CharField(default='', max_length=20)),
                ('LastName', models.CharField(default='', max_length=20)),
                ('vfmail', models.BooleanField(default=False)),
                ('history', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
    ]
