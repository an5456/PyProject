from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm1(forms.Form):
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    register2url = forms.CharField(label="注册第二页地址", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))

class RegisterForm2(forms.Form):
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    token = forms.CharField(label="令牌", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))

class setuserinfoForm(forms.Form):
    userid = forms.CharField(label="用户id", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # nickname = forms.CharField(label="昵称", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # paypassword = forms.CharField(label="支付密码", max_length=256,
                                # widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # telphone = forms.CharField(label="手机号", max_length=256,
                                #   widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))