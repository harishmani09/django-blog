# Generated by Django 4.2.7 on 2023-11-09 06:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogs", "0002_blog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="status",
            field=models.CharField(
                choices=[("draft", "Draft"), ("published", "Published")],
                default="draft",
                max_length=10,
            ),
        ),
    ]