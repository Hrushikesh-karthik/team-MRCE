# Generated by Django 3.2.25 on 2024-06-28 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0007_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
