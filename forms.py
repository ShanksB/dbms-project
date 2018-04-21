from django import forms
from .models import Student, FeesApplication

class RegisterStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('StudentName', 'Regno', 'BranchName', 'EmailId', 'Password')
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginStudentForm(forms.Form):
    username = forms.CharField(label="Enter Mail Id", widget=forms.TextInput(attrs={'class': 'form-control'}),
                               required=False)
    password = forms.CharField(label="Enter Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class FeesApplicationForm(forms.ModelForm):
    class Meta:
        model = FeesApplication
        fields = ('SemesterNo', 'DebitCardNo', 'Cvv', 'PaidFees')
        widgets = {
            'Cvv': forms.PasswordInput(),
        }