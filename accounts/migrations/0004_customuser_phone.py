# Generated by Django 4.0.1 on 2022-06-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_customuser_age_customuser_idgame'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]