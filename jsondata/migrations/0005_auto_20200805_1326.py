# Generated by Django 2.2.8 on 2020-08-05 11:26

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jsondata', '0004_storage_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='data',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
    ]
