# Generated by Django 5.0.2 on 2024-03-06 05:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('el', '0011_remove_chatgroup_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatgroup',
            name='creator',
        ),
        migrations.AddField(
            model_name='chatgroup',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]