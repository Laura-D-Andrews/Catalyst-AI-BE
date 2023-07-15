# Generated by Django 4.2.3 on 2023-07-15 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0008_delete_prompt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='sentiment',
            field=models.CharField(choices=[('harmony', 'harmony'), ('resilience', 'resilience'), ('fragility', 'fragility'), ('majesty', 'majesty'), ('serenity', 'serenity'), ('wonder', 'wonder'), ('transience', 'transience'), ('connection', 'connection'), ('solitude', 'solitude'), ('renewal', 'renewal')], default='', max_length=50),
        ),
    ]
