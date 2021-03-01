# Generated by Django 3.1.4 on 2021-02-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(default=' ', max_length=600)),
                ('authorId', models.CharField(default=' ', max_length=600)),
                ('authorName', models.CharField(default=' ', max_length=300)),
                ('assetUrl', models.CharField(default=' ', max_length=300)),
                ('imageUrl', models.CharField(default=' ', max_length=300)),
                ('thumbnailImageUrl', models.CharField(default=' ', max_length=300)),
                ('created_at', models.CharField(default=' ', max_length=300)),
                ('updated_at', models.CharField(default=' ', max_length=300)),
                ('releaseStatus', models.CharField(default=' ', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='vrcUser',
            fields=[
                ('id', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=300)),
                ('displayName', models.CharField(max_length=300)),
                ('bio', models.CharField(max_length=3000)),
                ('has_avatars', models.CharField(default='?', max_length=5)),
                ('fallbackAvatar', models.CharField(default='', max_length=300)),
                ('currentAvatarImageUrl', models.CharField(default='', max_length=300)),
                ('currentAvatarThumbnailImageUrl', models.CharField(default='', max_length=300)),
                ('last_platform', models.CharField(default='', max_length=300)),
                ('userIcon', models.CharField(default='', max_length=300)),
                ('tags', models.CharField(default='', max_length=300)),
                ('isFriend', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
