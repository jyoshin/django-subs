from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class SubscriptionForm(forms.Form):
    sub_name = forms.CharField(label='Subscription Name', max_length=100)
    price = forms.DecimalField(label='Price', max_digits=10, decimal_places=2)
    pay_date = forms.DateField(label='Payment Date', widget=forms.DateInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'sub_name',
            'price',
            'pay_date',
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )
