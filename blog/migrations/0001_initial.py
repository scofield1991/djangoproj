# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('birthday', models.DateField()),
                ('phone_number', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '999-9999999'.", regex='^[0-9]{3}-? ?[0-9]{7}$')])),
                ('image', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
