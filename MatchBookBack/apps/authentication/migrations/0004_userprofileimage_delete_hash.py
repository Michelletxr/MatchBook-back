# Generated by Django 4.1.3 on 2022-11-27 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_userprofileimage_user_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileimage',
            name='delete_hash',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
