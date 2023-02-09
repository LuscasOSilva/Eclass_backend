# Generated by Django 3.2.17 on 2023-02-09 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('e_class', '0003_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='students',
            name='Users_registrationID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_class.users'),
        ),
    ]
