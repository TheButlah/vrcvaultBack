# Generated by Django 3.1.4 on 2021-02-08 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vrcapi', '0002_avatar_user_checked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='description',
            field=models.CharField(default=' ', max_length=6000),
        ),
    ]