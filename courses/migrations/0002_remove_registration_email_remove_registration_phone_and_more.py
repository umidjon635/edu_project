# Generated by Django 5.2.4 on 2025-07-12 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='email',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='registered_at',
        ),
        migrations.AddField(
            model_name='registration',
            name='telegram_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registration',
            name='full_name',
            field=models.CharField(max_length=255),
        ),
    ]
