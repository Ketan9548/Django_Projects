# Generated by Django 5.0.2 on 2024-02-13 10:22

import back_end.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back_end', '0003_rename_code_room_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default=back_end.models.generate_unique_key, max_length=7, unique=True),
        ),
    ]
