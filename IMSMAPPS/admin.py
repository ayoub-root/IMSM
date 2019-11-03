from django.contrib import admin
from django import forms
from .models import Projects, Applications, Users, Components, Devices, Microservices, Data


class ProjectsAdminForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'


class ProjectsAdmin(admin.ModelAdmin):
    form = ProjectsAdminForm
    list_display = ['p_id', 'name', 'description', 'background', 'created', 'last_updated']
    readonly_fields = ['p_id', 'name', 'description', 'background', 'created', 'last_updated']


admin.site.register(Projects, ProjectsAdmin)


class ApplicationsAdminForm(forms.ModelForm):
    class Meta:
        model = Applications
        fields = '__all__'


class ApplicationsAdmin(admin.ModelAdmin):
    form = ApplicationsAdminForm
    list_display = ['a_id', 'name', 'description', 'category', 'background', 'created', 'last_updated']
    readonly_fields = ['a_id', 'name', 'description', 'category', 'background', 'created', 'last_updated']


admin.site.register(Applications, ApplicationsAdmin)


class UsersAdminForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'


class UsersAdmin(admin.ModelAdmin):
    form = UsersAdminForm
    list_display = ['u_id', 'email', 'firstname', 'lastname', 'password', 'address', 'birthday', 'avatar', 'type',
                    'created', 'last_updated']
    readonly_fields = ['u_id', 'email', 'firstname', 'lastname', 'password', 'address', 'birthday', 'avatar', 'type',
                       'created', 'last_updated']


admin.site.register(Users, UsersAdmin)


class ComponentsAdminForm(forms.ModelForm):
    class Meta:
        model = Components
        fields = '__all__'


class ComponentsAdmin(admin.ModelAdmin):
    form = ComponentsAdminForm
    list_display = ['c_id', 'name', 'description', 'background', 'created', 'last_updated']
    readonly_fields = ['c_id', 'name', 'description', 'background', 'created', 'last_updated']


admin.site.register(Components, ComponentsAdmin)


class DevicesAdminForm(forms.ModelForm):
    class Meta:
        model = Devices
        fields = '__all__'


class DevicesAdmin(admin.ModelAdmin):
    form = DevicesAdminForm
    list_display = ['d_id', 'name', 'description', 'type', 'created', 'last_updated']
    readonly_fields = ['d_id', 'name', 'description', 'type', 'created', 'last_updated']


admin.site.register(Devices, DevicesAdmin)


class MicroservicesAdminForm(forms.ModelForm):
    class Meta:
        model = Microservices
        fields = '__all__'


class MicroservicesAdmin(admin.ModelAdmin):
    form = MicroservicesAdminForm
    list_display = ['m_id', 'name', 'description', 'endpoint','type', 'cmd', 'creator', 'users', 'category', 'inputs', 'outputs',
                    'created', 'last_updated']
    readonly_fields = ['m_id', 'name', 'description', 'endpoint','type', 'cmd', 'creator', 'users', 'category', 'inputs', 'outputs',
                       'created', 'last_updated']


admin.site.register(Microservices, MicroservicesAdmin)


class DataAdminForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'


class DataAdmin(admin.ModelAdmin):
    form = DataAdminForm
    list_display = ['data_id', 'name', 'type', 'value', 'created', 'last_updated']
    readonly_fields = ['data_id', 'name', 'type', 'value', 'created', 'last_updated']


admin.site.register(Data, DataAdmin)
