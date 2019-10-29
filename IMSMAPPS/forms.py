from django import forms
from django.http import request

from .models import Projects, Applications, Users, Components, Devices, Microservices, Data



class ProjectsForm(forms.ModelForm):

    class Meta:


        model = Projects
        fields = [ 'name', 'description', 'background']



class ApplicationsForm(forms.ModelForm):
    class Meta:
        model = Applications

        fields = ['project','name', 'description', 'category', 'background']

class DateInput(forms.DateInput):
    input_type = 'date'
class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = [ 'firstname', 'lastname','email', 'password', 'address', 'birthday', 'avatar', 'type']
        widgets = {
            'password': forms.PasswordInput(),
            'birthday':DateInput(),
        }


class ComponentsForm(forms.ModelForm):
    class Meta:
        model = Components
        fields = ['application','name', 'description', 'background']


class DevicesForm(forms.ModelForm):
    class Meta:
        model = Devices
        fields = ['component','name', 'description', 'type','background']


class MicroservicesForm(forms.ModelForm):
    class Meta:
        model = Microservices
        fields = ['device','name', 'description', 'url', 'cmd', 'creator', 'users', 'category', 'inputs', 'outputs']


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name', 'type', 'value']
