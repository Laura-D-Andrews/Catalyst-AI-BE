# Generated by Django 4.2.3 on 2023-07-18 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0041_movement_length_visualart_length_write_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='length',
            field=models.CharField(choices=[('one word', 'one word'), ('three words', 'three words'), ('prompt', 'prompt')], default=''),
        ),
        migrations.AlterField(
            model_name='music',
            name='length',
            field=models.CharField(choices=[('one word', 'one word'), ('three words', 'three words'), ('prompt', 'prompt')], default=''),
        ),
        migrations.AlterField(
            model_name='visualart',
            name='length',
            field=models.CharField(choices=[('one word', 'one word'), ('three words', 'three words'), ('prompt', 'prompt')], default=''),
        ),
        migrations.AlterField(
            model_name='write',
            name='length',
            field=models.CharField(choices=[('one word', 'one word'), ('three words', 'three words'), ('prompt', 'prompt')], default=''),
        ),
    ]
