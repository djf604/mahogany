# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_page_background'),
        ('mahogany_theme', '0003_auto_20160111_0324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]
