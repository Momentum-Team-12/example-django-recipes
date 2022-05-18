# Generated by Django 4.1a1 on 2022-05-18 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_ingredient"),
    ]

    operations = [
        migrations.CreateModel(
            name="RecipeStep",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order",
                    models.PositiveIntegerField(
                        db_index=True, editable=False, verbose_name="order"
                    ),
                ),
                ("text", models.TextField()),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="steps",
                        to="core.recipe",
                    ),
                ),
            ],
            options={
                "ordering": ("order",),
                "abstract": False,
            },
        ),
    ]