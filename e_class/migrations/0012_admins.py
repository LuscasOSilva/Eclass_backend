# Generated by Django 4.1.6 on 2023-02-09 22:09

from django.db import migrations, models #type:ignore
import django.db.models.deletion #type:ignore


class Migration(migrations.Migration):

    dependencies = [
        ('e_class', '0011_teachers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('Users_registrationID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='e_class.users')),
            ],
            options={
                'ordering': ['Users_registrationID'],
            },
        ),
    ]
