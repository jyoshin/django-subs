from django.shortcuts import render, redirect, get_object_or_404
from .forms import SubscriptionForm
from .models import Subscription  

deleted_subscriptions = []

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
            form = SubscriptionForm()
    else:
        form = SubscriptionForm()

    subscriptions = Subscription.objects.all().order_by('sub_name')
    return render(request, 'base/home.html', {'form': form, 'subscriptions': subscriptions})

def delete_subscription(request, pk):
    global deleted_subscriptions

    subscription = get_object_or_404(Subscription, pk=pk)
    subsciption_data = {
        'sub_name': subscription.sub_name,
        'price': subscription.price,
        'pay_date': subscription.pay_date
    }

    deleted_subscriptions.append(subsciption_data)

    subscription.delete()
    
    return redirect('home')

def undo_last_delete(request):
    global deleted_subscriptions

    if deleted_subscriptions:
        last_deleted_subscription = deleted_subscriptions.pop()
        Subscription.objects.create(**last_deleted_subscription)
    
    return redirect('home')

