import enum
from django.db import models
import uuid
from buddy_groups.models import BuddyGroup
from buddy_profiles.models import BuddyProfile
from core.models import TimeStampedModel

def upload_to(instance, filename):
    return f'expenses/{filename}'


class BuddyExpense(TimeStampedModel):
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
    total_amount = models.DecimalField(verbose_name='Total amount', max_digits=8, decimal_places=3, default=0)

    currency = models.CharField(verbose_name='Currencies', max_length=64, choices=Currency.choices(), default=Currency.EUR)
    type_payment_distribution = models.CharField(verbose_name='Type of distribution for payments of expenses', max_length=64, choices=PaymentDistribution.choices(), default=PaymentDistribution.EQ)

    evicende_picture_url = models.ImageField(upload_to=upload_to, blank=True, null=True)

    payers = models.ManyToManyField(BuddyProfile, through="PayerPayments", related_name='payer_simplepayment')
    participants = models.ManyToManyField(BuddyProfile, through="SettleParticipantExpenseUp", related_name='participants_simplepayment')
    participants_of_expense_payment = models.ManyToManyField(BuddyProfile, through="ParticipantsOfExpensePayment", related_name='participants_of_expense_payment')


    def __str__(self):
        return f'{self.title} - {self.buddy_group}'

class PayerPayments(TimeStampedModel):
    who_do_simple_payment = models.ForeignKey(BuddyProfile, on_delete=models.CASCADE)
    what_expense_belong_to = models.ForeignKey(BuddyExpense, on_delete=models.CASCADE)

    amount_payment = models.DecimalField(verbose_name='Amount payment', max_digits=8, decimal_places=3, default=0)

    def __str__(self):
        return f'{self.who_do_simple_payment.full_name} - {self.what_expense_belong_to.title}'

class SettleParticipantExpenseUp(TimeStampedModel):
    who_settle_simple_payment_up = models.ForeignKey(BuddyProfile, on_delete=models.CASCADE)
    what_expense_belong = models.ForeignKey(BuddyExpense, on_delete=models.CASCADE)

    amount_payment = models.DecimalField(verbose_name='Amount payment', max_digits=8, decimal_places=3, default=0)


    def __str__(self):
        return f'{self.who_settle_simple_payment_up.full_name} - {self.what_expense_belong.title}'


class ParticipantsOfExpensePayment(TimeStampedModel):
    group_member = models.ForeignKey(BuddyProfile, on_delete=models.CASCADE)
    expense = models.ForeignKey(BuddyExpense, on_delete=models.CASCADE)
    percentage_to_pay = models.IntegerField(verbose_name='Percentage to pay')
    amount_to_pay = models.DecimalField(verbose_name='Amount to pay', max_digits=8, decimal_places=3,  default=0)
    payment_balance = models.DecimalField(verbose_name='Payment balance', max_digits=8, decimal_places=3, default=0)

    def __str__(self):
        return f'{self.group_member.full_name} - {self.expense.title}'

