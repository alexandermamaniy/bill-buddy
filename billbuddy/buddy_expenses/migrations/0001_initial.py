# Generated by Django 4.2.14 on 2024-10-23 16:18

import buddy_expenses.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuddyExpense',
            fields=[
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted_date', models.DateTimeField(blank=True, null=True, verbose_name='Deleted date')),
                ('is_active', models.BooleanField(default=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='description')),
                ('total_amount', models.DecimalField(decimal_places=3, default=0, max_digits=8, verbose_name='Total amount')),
                ('currency', models.CharField(choices=[('EUR', 'EUR'), ('USD', 'USD')], default=buddy_expenses.models.BuddyExpense.Currency['EUR'], max_length=64, verbose_name='Currencies')),
                ('type_payment_distribution', models.CharField(choices=[('EQUALLY', 'EQ'), ('UNEQUALLY', 'UNEQ'), ('PERCENTAGE', 'PER')], default=buddy_expenses.models.BuddyExpense.PaymentDistribution['EQ'], max_length=64, verbose_name='Type of distribution for payments of expenses')),
                ('evicende_picture_url', models.ImageField(blank=True, null=True, upload_to=buddy_expenses.models.upload_to)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ParticipantsOfExpensePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted_date', models.DateTimeField(blank=True, null=True, verbose_name='Deleted date')),
                ('is_active', models.BooleanField(default=True)),
                ('percentage_to_pay', models.IntegerField(verbose_name='Percentage to pay')),
                ('amount_to_pay', models.DecimalField(decimal_places=3, default=0, max_digits=8, verbose_name='Amount to pay')),
                ('payment_balance', models.DecimalField(decimal_places=3, default=0, max_digits=8, verbose_name='Payment balance')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentsMadeItByPayers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted_date', models.DateTimeField(blank=True, null=True, verbose_name='Deleted date')),
                ('is_active', models.BooleanField(default=True)),
                ('amount_payment', models.DecimalField(decimal_places=3, default=0, max_digits=8, verbose_name='Amount payment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SettlementByParticipants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted_date', models.DateTimeField(blank=True, null=True, verbose_name='Deleted date')),
                ('is_active', models.BooleanField(default=True)),
                ('amount_payment', models.DecimalField(decimal_places=3, default=0, max_digits=8, verbose_name='Amount payment')),
                ('what_expense_belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buddy_expenses.buddyexpense')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
