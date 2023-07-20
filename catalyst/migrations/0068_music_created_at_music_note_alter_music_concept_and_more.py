# Generated by Django 4.2.3 on 2023-07-19 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalyst', '0067_movement_created_at_movement_note_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2023-08-07'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='music',
            name='note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='music_notes', to='catalyst.note'),
        ),
        migrations.AlterField(
            model_name='music',
            name='concept',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='music',
            name='element',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='music',
            name='emotion',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='music',
            name='exploration',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]