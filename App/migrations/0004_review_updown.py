# Generated by Django 3.2.7 on 2021-10-07 10:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_rename_reviesws_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='updown',
            field=models.CharField(default=django.utils.timezone.now, max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
