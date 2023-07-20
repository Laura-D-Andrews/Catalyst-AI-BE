# Generated by Django 4.2.3 on 2023-07-20 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0077_definition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='text',
        ),
        migrations.AddField(
            model_name='movement',
            name='note',
            field=models.TextField(default='take notes'),
        ),
        migrations.AddField(
            model_name='music',
            name='note',
            field=models.TextField(default='take notes'),
        ),
        migrations.AddField(
            model_name='visualart',
            name='note',
            field=models.TextField(default='take notes'),
        ),
        migrations.AddField(
            model_name='write',
            name='note',
            field=models.TextField(default='take notes'),
        ),
    ]
