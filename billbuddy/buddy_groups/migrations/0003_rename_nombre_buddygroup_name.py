# Generated by Django 4.2.14 on 2024-08-01 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buddy_groups', '0002_groupmembers_groupadmins_buddygroup_group_admins_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buddygroup',
            old_name='nombre',
            new_name='name',
        ),
    ]