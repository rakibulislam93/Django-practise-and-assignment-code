from django import forms
from .models import TransactionsModel,TransferModel
from django.contrib.auth.models import User
from accounts.models import UserBankAccount

class TransactionsForm(forms.ModelForm):
    class Meta:
        model = TransactionsModel
        fields = ['amount','transactions_type']
    
    def __init__(self,*args,**kwargs):
        self.account = kwargs.pop('account') # account value ke pop kore anlam
        super().__init__(*args,**kwargs)

        self.fields['transactions_type'].disabled= True # ai field disable thakbe
        self.fields['transactions_type'].widget = forms.HiddenInput() # user er theke hide kora thakbe
    

    def save(self,commit=True):
        self.instance.account = self.account
        self.instance.balance_after_transactions = self.account.balance

        return super().save()


class DepositeForm(TransactionsForm):
    def clean_amount(self): # amount field ke filter korbo...
        min_deposite_amount = 100
        amount = self.cleaned_data.get('amount') # user er fill up kora form theke amra amount field er value ber korbo
          
        if amount<min_deposite_amount:
            raise forms.ValidationError(
                f'You need deposite at least {min_deposite_amount}'
            )
        return amount
    
class WithdrawForm(TransactionsForm):
    def clean_amount(self):
        min_withdraw_amount = 500
        max_withdraw_amount = 20000
        balance = self.account.balance
        amount = self.cleaned_data.get('amount')
        
        if amount<min_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at least {min_withdraw_amount}'
            )

        if amount > max_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at most {max_withdraw_amount}'
            )
        if amount > balance:
            raise forms.ValidationError(
                f'You have {balance} $ in your account'
                'You can not withdraw more than your account balance'
            )
        
        return amount

class LoanRequestForm(TransactionsForm):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')

        return amount
    


class TransferForm(forms.ModelForm):
    class Meta:
        model = TransferModel
        fields = ['recive_username','amount']

    def clean_recive_username(self):
        receive_username = self.cleaned_data.get('recive_username')
        if not User.objects.filter(username=receive_username).exists():
            raise forms.ValidationError('Account does not exist..')
        return receive_username