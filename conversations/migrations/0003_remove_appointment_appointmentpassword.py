# Generated by Django 4.0.1 on 2022-04-27 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0002_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appointmentPassword',
        ),
    ]
