from django.shortcuts import render
from balance.forms import TransactionForm
# Create your views here.


def transaction(request):
    user = request.user
    transaction_form = TransactionForm(user=user)
    context = {
        'transaction_form': transaction_form,
    }
    return render(request, 'balance/transaction.html', context)
