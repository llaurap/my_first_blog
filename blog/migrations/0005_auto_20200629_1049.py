# Generated by Django 2.2.12 on 2020-06-29 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200626_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='month',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
