# Generated by Django 5.2.1 on 2025-06-09 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_workexperience_end_date_workexperience_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='start_date',
            field=models.DateField(),
        ),
    ]
