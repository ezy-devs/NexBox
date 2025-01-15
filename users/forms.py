from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm

from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'password')

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'label': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
       }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].help_text = ''
    #     self.fields['username'].label = 'Email'

class UserUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('photo', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'state', 'postal_code', 'country', 'date_of_birth', 'bio')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields.pop('password', None)


class ResetPasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

    def __init__(self, user, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(user, *args, **kwargs)
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].help_text =''
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].help_text = ''