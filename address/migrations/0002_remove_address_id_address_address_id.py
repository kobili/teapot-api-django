# Generated by Django 4.2.1 on 2023-05-08 16:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='id',
        ),
        migrations.AddField(
            model_name='address',
            name='address_id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
