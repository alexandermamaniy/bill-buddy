# Generated by Django 4.2.14 on 2024-08-01 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buddy_groups', '0002_groupmembers_groupadmins_buddygroup_group_admins_and_more'),
        ('buddy_expenses', '0004_alter_buddyexpense_total_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipantsOfExpensePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage_to_pay', models.IntegerField(verbose_name='Percentage to pay')),
                ('amount_to_pay', models.DecimalField(decimal_places=3, max_digits=8, verbose_name='Amount to pay')),
                ('payment_balance', models.DecimalField(decimal_places=3, max_digits=8, verbose_name='Payment balance')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Created date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Modified date')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Deleted date')),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buddy_expenses.buddyexpense')),
                ('group_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buddy_groups.groupmembers')),
            ],
        ),
        migrations.AddField(
            model_name='buddyexpense',
            name='participants_of_expense_payment',
            field=models.ManyToManyField(related_name='participants_of_expense_payment', through='buddy_expenses.ParticipantsOfExpensePayment', to='buddy_groups.groupmembers'),
        ),
    ]
