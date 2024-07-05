from typing import Any
from django.contrib import admin
from . models import TransactionsModel,TransferModel
# Register your models here.

# admin.site.register(TransactionsModel)
admin.site.register(TransferModel)
@admin.register(TransactionsModel)

class TransacionAdmin(admin.ModelAdmin):
    list_display = ['account','amount','balance_after_transactions','transactions_type','loan_approve']

    def save_model(self,request,obj,form,change):
        obj.account.balance += obj.amount
        obj.balance_after_transactios = obj.account.balance
        obj.account.save()
        super().save_model(request,obj,form,change)