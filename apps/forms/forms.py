from django import forms

from forms import models


class BaseRequestForm(forms.ModelForm):
    """Base request forms class"""
    class Meta:
        fields = '__all__'
        exclude = ('read_status',)


class FeedbackForm(BaseRequestForm):
    class Meta:
        fields = '__all__'
        exclude = ('read_status',)
        model = models.Feedback

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['phone_number'].required = True


class OrderForm(BaseRequestForm):
    class Meta:
        fields = '__all__'
        exclude = ('read_status',)
        model = models.Order

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['phone_number'].required = True
        self.fields['role'].required = True


class SubscribeForm(BaseRequestForm):
    class Meta:
        fields = '__all__'
        exclude = ('read_status',)
        model = models.Subscribe
