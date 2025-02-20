# Generated by Django 5.0.6 on 2024-07-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feedback", "0003_question"),
    ]

    operations = [
        migrations.AddField(
            model_name="feedback",
            name="semester",
            field=models.IntegerField(
                choices=[
                    (1, "1st Semester"),
                    (2, "2nd Semester"),
                    (3, "3rd Semester"),
                    (4, "4th Semester"),
                    (5, "5th Semester"),
                    (6, "6th Semester"),
                    (7, "7th Semester"),
                    (8, "8th Semester"),
                ],
                default=1,
            ),
        ),
        migrations.AddField(
            model_name="feedback",
            name="teacher",
            field=models.CharField(
                choices=[
                    ("teacher1", "Dr. John Doe"),
                    ("teacher2", "Dr. Jane Smith"),
                    ("teacher3", "Prof. Richard Roe"),
                    ("teacher4", "Prof. Mary Major"),
                    ("teacher5", "Dr. Alan Smithee"),
                ],
                default="teacher1",
                max_length=10,
            ),
        ),
    ]
