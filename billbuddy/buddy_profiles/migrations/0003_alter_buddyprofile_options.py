# Generated by Django 4.2.14 on 2024-07-29 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buddy_profiles', '0002_buddyprofile_created_date_buddyprofile_delete_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buddyprofile',
            options={'verbose_name': 'Buddy Profile', 'verbose_name_plural': 'Buddy Profiles'},
        ),
    ]
