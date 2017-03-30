# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='url',
            fields=[
                ('url', models.CharField(max_length=1000)),
                ('shorturl', models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
