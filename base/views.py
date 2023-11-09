from django.shortcuts import render, redirect
from .forms import SubscriptionForm
from .models import Subscription  

def subscription_view(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = Subscription(
                sub_name=form.cleaned_data['sub_name'],
                price=form.cleaned_data['price'],
                pay_date=form.cleaned_data['pay_date']
            )
            subscription.save()  
    else:
        form = SubscriptionForm()

    subscriptions = Subscription.objects.all().order_by('sub_name')
    return render(request, 'base/home.html', {'form': form, 'subscriptions': subscriptions})
