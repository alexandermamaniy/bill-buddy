from django.contrib import admin
from buddy_expenses.models import *

class payer_payments_inline(admin.TabularInline):
    model = PayerPayments
    extra = 1

class settle_participant_expense_up__inline(admin.TabularInline):
    model = SettleParticipantExpenseUp
    extra = 1


class participants_of_expense_payment_inline(admin.TabularInline):
    model = ParticipantsOfExpensePayment
    extra = 1

@admin.register(BuddyExpense)
class BuddyExpenseAdmin(admin.ModelAdmin):
    # filter_horizontal = ("group_members",)
    inlines = (payer_payments_inline, settle_participant_expense_up__inline, participants_of_expense_payment_inline,)

admin.site.register(PayerPayments)
admin.site.register(SettleParticipantExpenseUp)
admin.site.register(ParticipantsOfExpensePayment)


