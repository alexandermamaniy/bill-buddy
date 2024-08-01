# Generated by Django 4.2.14 on 2024-08-01 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buddy_groups', '0003_rename_nombre_buddygroup_name'),
        ('buddy_expenses', '0007_rename_who_do_simple_payment_settleparticipantexpenseup_who_settle_simple_payment_up'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simplepayment',
            name='buddy_payer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buddy_groups.groupmembers', verbose_name='Buddy payer'),
        ),
    ]