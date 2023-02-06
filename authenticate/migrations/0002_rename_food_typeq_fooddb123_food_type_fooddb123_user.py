# Generated by Django 4.1.2 on 2022-10-29 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fooddb123',
            old_name='food_typeq',
            new_name='food_type',
        ),
        migrations.AddField(
            model_name='fooddb123',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='form', to=settings.AUTH_USER_MODEL),
        ),
    ]
