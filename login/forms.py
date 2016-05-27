from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required



class LoginForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')

        super(LoginForm, self).__init__(*args, **kwargs)

    def login_in(self):
        # send email using the self.cleaned_data dictionary
        data = self.cleaned_data
        user = authenticate(username= data['name'], password=data['password'])
        if user is not None:
            # the password verified for the user
            if user.is_active:
                login(self.request, user)
                print("User is valid, active and authenticated")
            else:
                print("The password is valid, but the account has been disabled!")
        else:
            # the authentication system was unable to verify the username and password
            print "request.user:",self.request.user
            print("The username and password were incorrect.")


