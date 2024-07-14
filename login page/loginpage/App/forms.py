from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30, error_messages={'required': 'Username is required'})
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required': 'Password is required'})

    def clean_username(self):
        username = self.cleaned_data['username']
        if username.lower() == 'admin':
            raise forms.ValidationError("This username is reserved.")
        return username