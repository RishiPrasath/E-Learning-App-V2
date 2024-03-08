# Generated by Django 5.0.2 on 2024-03-07 09:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('el', '0012_remove_chatgroup_creator_chatgroup_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('review', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_received', to='el.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_given', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
