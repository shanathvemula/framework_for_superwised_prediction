# Generated by Django 3.0.4 on 2020-04-07 16:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200407_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='images',
            field=models.FileField(blank=True, error_messages={'csv': 'file Extension must be csv'}, help_text='Browse the file here It  accepts only csv files only', upload_to='files', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['CSV'])]),
        ),
    ]
