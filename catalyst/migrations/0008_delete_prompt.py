# Generated by Django 4.2.3 on 2023-07-15 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0007_remove_prompt_poem_prompt_inputs'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Prompt',
        ),
    ]
