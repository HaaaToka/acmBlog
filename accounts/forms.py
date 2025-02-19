from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class LoginForm(forms.Form):

    username=forms.CharField(max_length=100, label = "Account Name")
    password=forms.CharField(max_length=100, label="Password", widget=forms.PasswordInput)

    def clean(self):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username='username', password='password')
            if user:
                raise forms.ValidationError('Kullanıcı adı yada parola yanlıs')
        return super(LoginForm,self).clean()


class RegisterForm(forms.ModelForm):
    # captcha = ReCaptchaField()

    username=forms.CharField(max_length=100, label = "Account Name")
    first_name=forms.CharField(max_length=100, label="First Name")
    last_name=forms.CharField(max_length=100,label="Last Name")
    password1=forms.CharField(max_length=100, label="Password", widget=forms.PasswordInput)
    password2=forms.CharField(max_length=100, label="Password Again", widget=forms.PasswordInput)
    e_mail=forms.CharField(max_length=120,label="EMail")

    class Meta:
        model=User
        fields=[
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'e_mail'
        ]

    def clean_password2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords not  same")
        return password2
