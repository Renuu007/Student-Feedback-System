# Generated by Django 5.0.6 on 2024-07-15 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feedback", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="feedback",
            name="pdf_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
