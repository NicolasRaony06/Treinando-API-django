# Generated by Django 5.0.6 on 2024-06-01 00:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "nickname",
                    models.CharField(
                        default="NoNickname",
                        max_length=80,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(default="NoName", max_length=120)),
                (
                    "email",
                    models.EmailField(default="noemail@email.com", max_length=254),
                ),
                ("age", models.IntegerField(default=0)),
            ],
        ),
    ]
