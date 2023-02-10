# Generated by Django 4.1.6 on 2023-02-09 21:39

from django.db import migrations, models #type:ignore
import django.db.models.deletion #type:ignore


class Migration(migrations.Migration):

    dependencies = [
        ('e_class', '0010_auto_20230209_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('Users_registrationID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='e_class.users')),
                ('specialization', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ['Users_registrationID'],
            },
        ),
    ]
