# Generated by Django 5.2.4 on 2025-07-23 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_desk_options_alter_library_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='desk',
            name='qr_sent',
            field=models.BooleanField(default=False),
        ),
    ]
