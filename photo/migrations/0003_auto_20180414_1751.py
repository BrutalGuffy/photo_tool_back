# Generated by Django 2.0.3 on 2018-04-14 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20180414_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='char_tag',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='int_tag',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='time_tag',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
