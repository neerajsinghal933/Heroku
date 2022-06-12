# Generated by Django 3.2.8 on 2022-04-04 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageData',
            fields=[
                ('messageID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('messageBody', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('messageImage', models.ImageField(blank=True, null=True, upload_to='')),
                ('isRead', models.BooleanField(default=False, null=True)),
                ('recieverProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RecieverInConversation', to=settings.AUTH_USER_MODEL)),
                ('senderProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SenderInConversation', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['isRead', '-created'],
            },
        ),
    ]
