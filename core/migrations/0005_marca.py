# Generated by Django 5.0.6 on 2024-07-02 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_cor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Marca",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("descricao", models.CharField(max_length=50)),
                ("nacionalidade", models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
