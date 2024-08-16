# Generated by Django 4.2.14 on 2024-08-06 13:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('buddy_expenses', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buddyexpense',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='buddyexpense',
            name='deleted_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Deleted date'),
        ),
        migrations.AlterField(
            model_name='buddyexpense',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='participantsofexpensepayment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='participantsofexpensepayment',
            name='deleted_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Deleted date'),
        ),
        migrations.AlterField(
            model_name='participantsofexpensepayment',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='payerpayments',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='payerpayments',
            name='deleted_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Deleted date'),
        ),
        migrations.AlterField(
            model_name='payerpayments',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='settleparticipantexpenseup',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='settleparticipantexpenseup',
            name='deleted_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Deleted date'),
        ),
        migrations.AlterField(
            model_name='settleparticipantexpenseup',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
