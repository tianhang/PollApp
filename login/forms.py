from django import forms


class LoginForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField()

    def login_in(self):
        # send email using the self.cleaned_data dictionary
        print 'login in ................'
        pass