# Generated by Django 2.1 on 2018-08-30 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180829_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
