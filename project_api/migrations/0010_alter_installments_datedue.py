# Generated by Django 4.1.1 on 2022-10-10 09:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project_api', '0009_alter_installments_datedue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installments',
            name='dateDue',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]