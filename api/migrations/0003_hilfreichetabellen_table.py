# Generated by Django 3.2.3 on 2021-05-27 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210526_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='hilfreichetabellen',
            name='table',
            field=models.JSONField(blank=True, null=True),
        ),
    ]