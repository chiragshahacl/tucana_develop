# Generated by Django 4.1.10 on 2024-05-28 15:47

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Variable",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "key",
                    models.CharField(max_length=150, unique=True, verbose_name="key"),
                ),
                ("value", models.CharField(max_length=150, verbose_name="value")),
            ],
            options={
                "verbose_name": "variable",
                "verbose_name_plural": "variables",
                "ordering": ["key"],
            },
        ),
    ]
