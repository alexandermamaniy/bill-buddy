import enum
from django.db import models
import uuid
from buddy_groups.models import BuddyGroup, GroupMembers
from buddy_profiles.models import BuddyProfile

def upload_to(instance, filename):
    return f'expenses/{filename}'


class SimplePayment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    buddy_payer = models.ForeignKey(BuddyProfile, on_delete=models.CASCADE, verbose_name='Buddy payer')
    amount_payment = models.DecimalField(verbose_name='Amount payment', max_digits=8, decimal_places=3)
    # expose this field
    created_date = models.DateField(verbose_name='Created date', auto_now=False, auto_now_add=True)
    modified_date = models.DateField(verbose_name='Modified date', auto_now=True, auto_now_add=False)
    delete_date = models.DateField(verbose_name='Deleted date', auto_now=True, auto_now_add=False)


class BuddyExpense(models.Model):
    @enum.unique
    class Currency(str, enum.Enum):
        EUR = 'EUR'
        USD = 'USD'

        @classmethod
        def choices(cls):
            return [(item.value, item.name) for item in cls]

    @enum.unique
    class PaymentDistribution(str, enum.Enum):
        EQ = 'EQUALLY'
        UNEQ = 'UNEQUALLY'
        PER = 'PERCENTAGE'

        @classmethod
        def choices(cls):
            return [(item.value, item.name) for item in cls]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='title', max_length=255, blank=False, null=False)
    buddy_group = models.ForeignKey(BuddyGroup, on_delete=models.CASCADE, verbose_name='Buddy group')
    description = models.CharField(verbose_name='description', max_length=255, blank=True, null=False)
    total_amount = models.DecimalField(verbose_name='Total amount', max_digits=8, decimal_places=3)

    currency = models.CharField(verbose_name='Currencies', max_length=64, choices=Currency.choices(), default=Currency.EUR)
    type_payment_distribution = models.CharField(verbose_name='Type of distribution for payments of expenses', max_length=64, choices=PaymentDistribution.choices(), default=PaymentDistribution.EQ)

    evicende_picture_url = models.ImageField(upload_to=upload_to, blank=True, null=True)

    payers = models.ManyToManyField(SimplePayment, through="PayerPayments", related_name='payer_simplepayment')
    participants = models.ManyToManyField(SimplePayment, through="SettleParticipantExpenseUp", related_name='participants_simplepayment')
    participants_of_expense_payment = models.ManyToManyField(GroupMembers, through="ParticipantsOfExpensePayment", related_name='participants_of_expense_payment')

    # expose this field
    created_date = models.DateField(verbose_name='Created date', auto_now=False, auto_now_add=True)
    # expose this field
    modified_date = models.DateField(verbose_name='Modified date', auto_now=True, auto_now_add=False)
    delete_date = models.DateField(verbose_name='Deleted date', auto_now=True, auto_now_add=False)


    def __str__(self):
        return f'{self.title} - {self.buddy_group}'

class PayerPayments(models.Model):
    who_do_simple_payment = models.ForeignKey(SimplePayment, on_delete=models.CASCADE)
    what_expense_belong_to = models.ForeignKey(BuddyExpense, on_delete=models.CASCADE)
    # expose this field
    created_date = models.DateField(verbose_name='Created date', auto_now=False, auto_now_add=True)
    # expose this field
    modified_date = models.DateField(verbose_name='Modified date', auto_now=True, auto_now_add=False)
    delete_date = models.DateField(verbose_name='Deleted date', auto_now=True, auto_now_add=False)

class SettleParticipantExpenseUp(models.Model):
    who_settle_simple_payment_up = models.ForeignKey(SimplePayment, on_delete=models.CASCADE)
    what_expense_belong = models.ForeignKey(BuddyExpense, on_delete=models.CASCADE)
    # expose this field
    created_date = models.DateField(verbose_name='Created date', auto_now=False, auto_now_add=True)
    # expose this field
    modified_date = models.DateField(verbose_name='Modified date', auto_now=True, auto_now_add=False)
    delete_date = models.DateField(verbose_name='Deleted date', auto_now=True, auto_now_add=False)



class ParticipantsOfExpensePayment(models.Model):
    group_member = models.ForeignKey(GroupMembers, on_delete=models.CASCADE)
    expense = models.ForeignKey(BuddyExpense, on_delete=models.CASCADE)
    percentage_to_pay = models.IntegerField(verbose_name='Percentage to pay')
    amount_to_pay = models.DecimalField(verbose_name='Amount to pay', max_digits=8, decimal_places=3)
    payment_balance = models.DecimalField(verbose_name='Payment balance', max_digits=8, decimal_places=3)

    created_date = models.DateField(verbose_name='Created date', auto_now=False, auto_now_add=True)
    modified_date = models.DateField(verbose_name='Modified date', auto_now=True, auto_now_add=False)
    delete_date = models.DateField(verbose_name='Deleted date', auto_now=True, auto_now_add=False)

