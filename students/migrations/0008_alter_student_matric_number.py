# Generated by Django 5.1.1 on 2024-10-18 13:15

import students.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_alter_student_matric_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='matric_number',
            field=models.PositiveBigIntegerField(validators=[students.models.nine_digit_validator]),
        ),
    ]
