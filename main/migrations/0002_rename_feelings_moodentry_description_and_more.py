# Generated by Django 5.1.1 on 2024-09-10 07:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="moodentry",
            old_name="feelings",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="moodentry",
            old_name="mood",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="moodentry",
            old_name="mood_intensity",
            new_name="price",
        ),
        migrations.RemoveField(
            model_name="moodentry",
            name="time",
        ),
    ]
