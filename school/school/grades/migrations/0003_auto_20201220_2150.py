# Generated by Django 3.1.4 on 2020-12-21 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0002_auto_20201220_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='born_date',
            field=models.DateField(),
        ),
    ]