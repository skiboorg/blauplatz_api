# Generated by Django 3.2.3 on 2021-05-26 19:42

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HilfreicheTabellen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('name_slug', models.CharField(blank=True, db_index=True, editable=False, max_length=255, null=True)),
                ('file', models.FileField(upload_to='tabellen/', verbose_name='Table')),
            ],
        ),
        migrations.AlterField(
            model_name='richtungen',
            name='icon',
            field=models.ImageField(upload_to='richtungen/', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='richtungen',
            name='image',
            field=models.ImageField(upload_to='richtungen/', verbose_name='Top image'),
        ),
        migrations.AlterField(
            model_name='richtungen',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='richtungen',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Page text'),
        ),
    ]