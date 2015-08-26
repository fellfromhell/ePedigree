from django.contrib import admin
from django.forms.widgets import DateInput

__author__ = 'vivincyriac'
from django.forms import ModelForm, HiddenInput
from epedigree.models import Item, Order, OrderLines, Lot, LotTransactions, Client


class ClientPostForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class ItemPostForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class OrderPostForm(ModelForm):
    class Meta:
        model = Order
        fields = ['title', 'orderDate', 'description', 'clientID', 'status']
        widgets = {
            'orderDate': DateInput(attrs={'type':'date'}),
        }

class OrderLinesPostForm(ModelForm):
    class Meta:
        model = OrderLines
        fields = ['order', 'item', 'lotnum', 'amount', 'measurement']
        widgets = {'order': HiddenInput()}


class LotPostForm(ModelForm):
    class Meta:
        model = Lot
        fields = ['lotNumber', 'item', 'expiryDate', 'ndc', 'description', 'status']
        widgets = {
            'expiryDate': DateInput(attrs={'type':'date'}),
        }

class LotCertifyForm(ModelForm):
    class Meta:
        model = Lot
        exclude = ["user"]
        fields = ['status']


class LotTransactionsPostForm(ModelForm):
    class Meta:
        model = LotTransactions
        fields = ['lot', 'soldToName', 'soldToAddressLine1', 'soldToAddressLine2', \
                  'soldToCity', 'soldToState', 'soldToPostalCode', 'shipToName', 'shipToAddressLine1',\
                  'shipToAddressLine2', 'shipToCity', 'shipToState', 'shipToPostalCode']
        # widgets = {'lot': HiddenInput()}