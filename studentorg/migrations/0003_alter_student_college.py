# Generated by Django 5.0.1 on 2024-10-30 07:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentorg', '0002_student_college'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='college',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='studentorg.college'),
        ),
    ]
