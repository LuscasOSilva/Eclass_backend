# Generated by Django 4.1.6 on 2023-02-12 20:16

from django.db import migrations, models #type: ignore


class Migration(migrations.Migration):
    dependencies = [
        ("e_class", "0032_classes_students"),
    ]

    operations = [
        migrations.AlterField(
            model_name="multiplequestion",
            name="option3",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="multiplequestion",
            name="option4",
            field=models.TextField(blank=True, null=True),
        ),
    ]
