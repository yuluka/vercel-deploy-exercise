# Generated by Django 4.2.5 on 2023-09-10 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='courses.professor'),
        ),
    ]
