# Generated by Django 3.0.5 on 2020-05-22 02:20

import django.core.validators
from django.db import migrations, models
import report.models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_auto_20200521_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Template name', max_length=100, unique=True)),
                ('template', models.FileField(help_text='Report template file', upload_to=report.models.rename_template, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['html', 'htm', 'tex'])])),
                ('description', models.CharField(help_text='Report template description', max_length=250)),
                ('filters', models.CharField(blank=True, help_text='Query filters (comma-separated list of key=value pairs)', max_length=250, validators=[report.models.validate_filter_string])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='reporttemplate',
            name='template',
            field=models.FileField(help_text='Report template file', upload_to=report.models.rename_template, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['html', 'htm', 'tex'])]),
        ),
    ]
