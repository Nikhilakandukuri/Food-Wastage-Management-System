# Generated by Django 3.0.5 on 2022-11-11 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_auto_20221111_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooddb123',
            name='quantity',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
