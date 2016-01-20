# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahogany_theme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
                ('time', models.DateTimeField()),
                ('location', models.CharField(max_length=512)),
                ('details', models.TextField()),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
