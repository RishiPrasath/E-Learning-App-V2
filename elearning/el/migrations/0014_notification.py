# Generated by Django 5.0.2 on 2024-03-08 02:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('el', '0013_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('redirectURL', models.CharField(blank=True, max_length=255, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('recipients', models.ManyToManyField(related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
