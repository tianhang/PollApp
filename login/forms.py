from django import forms


class LoginForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(LoginForm, self).__init__(*args, **kwargs)

    def login_in(self):
        # send email using the self.cleaned_data dictionary
        ##print self.cleaned_data
        pass

