# Generated by Django 4.1.6 on 2023-02-11 03:56

from django.db import migrations, models # type: ignore
import django.db.models.deletion # type: ignore


class Migration(migrations.Migration):
    dependencies = [
        ("e_class", "0014_admin_student_subject_teacher_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Classes",
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
                ("name", models.CharField(max_length=15)),
                ("size", models.IntegerField()),
                ("startTime", models.DateField()),
                ("endTime", models.DateField()),
                ("period", models.IntegerField()),
                ("password", models.CharField(max_length=30)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.RenameField(
            model_name="subject",
            old_name="admin_id",
            new_name="admin",
        ),
        migrations.AddField(
            model_name="subject",
            name="teachers",
            field=models.ManyToManyField(to="e_class.teacher"),
        ),
        migrations.CreateModel(
            name="Students_has_Classes",
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
                ("registerDate", models.DateField(auto_now_add=True)),
                (
                    "classes",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="e_class.classes",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="e_class.student",
                    ),
                ),
            ],
            options={
                "ordering": ["registerDate"],
            },
        ),
        migrations.AddField(
            model_name="classes",
            name="students",
            field=models.ManyToManyField(
                through="e_class.Students_has_Classes", to="e_class.student"
            ),
        ),
        migrations.AddField(
            model_name="classes",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="e_class.subject"
            ),
        ),
    ]
