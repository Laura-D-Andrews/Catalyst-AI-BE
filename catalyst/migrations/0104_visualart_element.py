# Generated by Django 4.2.3 on 2023-07-31 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0103_alter_movement_prompt_length_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='visualart',
            name='element',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
