# Generated by Django 4.2.1 on 2023-06-02 20:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("control", "0002_remove_enrollment_teacher"),
    ]

    operations = [
        migrations.AlterField(
            model_name="enrollment",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
