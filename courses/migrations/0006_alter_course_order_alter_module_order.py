# Generated by Django 5.1.7 on 2025-03-07 01:58

import courses.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_module_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='order',
            field=courses.fields.OrderField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='order',
            field=courses.fields.OrderField(blank=True, null=True),
        ),
    ]
