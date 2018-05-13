from django import forms
from .models import Student, FeesApplication

class RegisterStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('StudentName', 'Regno', 'BranchName', 'EmailId', 'Password')

        BRANCHES = (
            ('cse', 'ComputerScience'),
            ('mech', 'MechanicalEngineering'),
            ('ece', 'ElectronicsAndCommunication')	#add more branches.... :)
        )
        widgets = {
            'Password': forms.PasswordInput(attrs={'class':'form-control'}),
            'StudentName': forms.TextInput(attrs={'class':'form-control'}),
            'Regno': forms.TextInput(attrs={'class':'form-control'}),
            'BranchName': forms.Select(attrs={'class':'form-control'}),
            'EmailId': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {
            'StudentName': "Student Name ",
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
            'Cvv': forms.PasswordInput(attrs={'class':'form-control'}),
            'SemesterNo': forms.Select(attrs={'class':'form-control'}),
            'DebitCardNo': forms.TextInput(attrs={'class':'form-control'}),
            'PaidFees': forms.TextInput(attrs={'class':'form-control'}), 
        }