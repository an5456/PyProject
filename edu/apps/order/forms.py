from django import forms

# Create your views here.
class addorderForm(forms.Form):
    userid = forms.CharField(label="用户id", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    courseid = forms.CharField(label="课程id", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    total_amount = forms.CharField(label="价钱", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    discount = forms.CharField(label="折扣价钱", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))

class payorderForm(forms.Form):
    orderid = forms.CharField(label="订单id", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pay_method = forms.CharField(label="付款方式", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))

