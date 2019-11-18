from django.contrib.auth import authenticate
from django.forms.forms import BaseForm
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.views.generic.base import TemplateView

from IMSMAPPS import forms
from .models import Projects, Applications, Users, Components, Devices, Microservices, Data
from .forms import ProjectsForm, ApplicationsForm, UsersForm, ComponentsForm, DevicesForm, MicroservicesForm, DataForm


class index(TemplateView):
    template_name = "apps.html"


class login(TemplateView):
    template_name = "loginregister.html"


class apps(TemplateView):
    template_name = "apps.html"


def showadata(request):
    # print(request.POST['obj'])
    if request.method == 'POST':
        print(request.POST['obj'])
        if (request.POST['obj'] == "projects"):
            inputs = {'data': list(Projects.objects.values()), 'link': "projects/create/",
                      'linkdel': "projects/delete/", 'linkupd': "projects/update/", 'option': "project"}
        if (request.POST['obj'] == "applications"):
            inputs = {'data': list(Applications.objects.values()), 'link': "applications/create/",
                      'linkdel': "applications/delete/", 'linkupd': "applications/update/",'linkbuild': "applications/building/", 'option': "application" }
        if (request.POST['obj'] == "users"):
            inputs = {'data': list(Users.objects.values()), 'link': "users/create/", 'linkdel': "users/delete/",
                      'linkupd': "users/update/", 'option': "user"}
        if (request.POST['obj'] == "components"):
            inputs = {'data': list(Components.objects.values()), 'link': "components/create/",
                      'linkdel': "components/delete/", 'linkupd': "components/update/", 'option': "component"}
        if (request.POST['obj'] == "devices"):
            inputs = {'data': list(Devices.objects.values()), 'link': "devices/create/", 'linkdel': "devices/delete/",
                      'linkupd': "devices/update/", 'option': "device"}
        if (request.POST['obj'] == "microservices"):
            inputs = {'data': list(Microservices.objects.values()), 'link': "microservices/create/",
                      'linkdel': "microservices/delete/", 'linkupd': "microservices/update/", 'option': "microservice"}
        if (request.POST['obj'] == "data"):
            inputs = {'data': list(Data.objects.values()), 'link': "data/create/", 'linkdel': "data/delete/",
                      'linkupd': "data/update/", 'option': "data"}

        return render(request, 'IMSMAPPS/datashow.html', inputs)


def dataregister(request):
    if request.method == 'POST':
        print("kkkkkkkkkkkkkkkkkkkkkk "+request.POST['obj'])
        if (request.POST['obj'] == "project"):
            form_class = ProjectsForm
            inputs = {'form': form_class, 'link': "projects/created/"}
        if (request.POST['obj'] == "application"):
            form_class = ApplicationsForm
            inputs = {'form': form_class, 'link': "applications/created/"}
        if (request.POST['obj'] == "user"):
            form_class = UsersForm
            inputs = {'form': form_class, 'link': "users/created/"}
        if (request.POST['obj'] == "component"):
            form_class = ComponentsForm
            inputs = {'form': form_class, 'link': "components/created/"}
        if (request.POST['obj'] == "device"):
            form_class = DevicesForm
            inputs = {'form': form_class, 'link': "devices/created/"}
        if (request.POST['obj'] == "microservice"):
            form_class = MicroservicesForm
            inputs = {'form': form_class, 'link': "microservices/created/"}
        if (request.POST['obj'] == "data"):
            form_class = DataForm
            inputs = {'form': form_class, 'link': "data/created/"}

        return render(request, 'IMSMAPPS/dataregiser.html', inputs)
def datasave(request):
    if request.POST:
        print("zzzzzzzzz "+str(request.POST))
        form= object()
        if (request.path == "/projects/created/"):
            obj = ProjectsForm(request.POST,request.FILES)
            if obj.is_valid():
                x = Users.objects.get(u_id=request.session['user_id'])
                # form.cleaned_data['userid'] = x
                print(str(x) + "  -------------   " + str(obj))
                form = obj.save(commit=False)
                form.userid = x
            #print("ssssssssssssssssss   "+str(form))
          #  form.cleaned_data['userid']=request.session['user_id']
        if (request.path == "/applications/created/"):
            obj = ApplicationsForm(request.POST,request.FILES)
            #obj = ProjectsForm(request.POST, request.FILES)
            if obj.is_valid():
                x = Users.objects.get(u_id=request.session['user_id'])
                y = Projects.objects.get(userid=request.session['user_id'])
                # form.cleaned_data['userid'] = x
                print(str(x) + "  -------------   " + str(obj))
                form = obj.save(commit=False)
                form.userid = x
                form.project= y
        if (request.path == "/users/created/"):
            form = UsersForm(request.POST,request.FILES)
        if(request.path=="/components/created/"):
            form = ComponentsForm(request.POST,request.FILES)
        if (request.path == "/devices/created/"):
            form = DevicesForm(request.POST,request.FILES)
        if (request.path == "/microservices/created/"):
            form = MicroservicesForm(request.POST,request.FILES)
        if (request.path == "/data/created/"):
            form = DataForm(request.POST,request.FILES)

        if request.path == "/projects/created/" or  request.path == "/applications/created/" :
            form.save()
            return HttpResponse("succesuflly enrgisitred <br/> please refreche")
        elif form.is_valid():
            form.save()
            return HttpResponse("succesuflly enrgisitred <br/> please refreche")
        else:
            return JsonResponse({'error':form.errors})
def dataresave(request):
    if request.POST:
        print("zzzzzzzzz "+request.POST['id'])
        form= object()
        if (request.path == "/projects/updated/"):
            form = ProjectsForm(request.POST,request.FILES,instance=Projects.objects.get(pk=request.POST['id']))
        if (request.path == "/applications/updated/"):
            form = ApplicationsForm(request.POST,request.FILES,instance=Applications.objects.get(pk=request.POST['id']))
        if (request.path == "/users/updated/"):
            form = UsersForm(request.POST,request.FILES,instance=Users.objects.get(pk=request.POST['id']))
        if(request.path=="/components/updated/"):
            form = ComponentsForm(request.POST,request.FILES,instance=Components.objects.get(pk=request.POST['id']))
        if (request.path == "/devices/updated/"):
            form = DevicesForm(request.POST,request.FILES,instance=Devices.objects.get(pk=request.POST['id']))
        if (request.path == "/microservices/updated/"):
            form = MicroservicesForm(request.POST,request.FILES,instance=Microservices.objects.get(pk=request.POST['id']))
        if (request.path == "/data/updated/"):
            form = DataForm(request.POST,request.FILES,instance=Data.objects.get(pk=request.POST['id']))

        if form.is_valid():
            form.save()
            return HttpResponse("succesuflly enrgisitred <br/> please refreche")
        else:
            return JsonResponse({'error':form.errors})

def datadelete(request):
    if request.POST:
        print("delete "+request.POST['id'])
        form= object()
        if (request.path == "/projects/delete/"):
            form=Projects.objects.filter(pk=request.POST['id']).delete()
        if (request.path == "/applications/delete/"):
            form = Applications.objects.filter(pk=request.POST['id']).delete()
        if (request.path == "/users/delete/"):
            form = Users.objects.filter(pk=request.POST['id']).delete()
        if(request.path=="/components/delete/"):
            form = Components.objects.filter(pk=request.POST['id']).delete()
        if (request.path == "/devices/delete/"):
            form = Devices.objects.filter(pk=request.POST['id']).delete()
        if (request.path == "/microservices/delete/"):
            form = Microservices.objects.filter(pk=request.POST['id']).delete()
        if (request.path == "/data/delete/"):
            form = Data.objects.filter(pk=request.POST['id']).delete()

        if form:
            return HttpResponse("succesuflly deleted <br/> please refresh"+str(form))
        else:
            return JsonResponse({'error':form.errors})


def dataupdate(request):
    if request.method == 'POST':
        print("qqqqqqqqq " + request.POST['obj'] + "  " + request.POST['pk'])
        if (request.POST['obj'] == "project"):
            model = Projects.objects.get(pk=request.POST['pk'])
            form_class = ProjectsForm(instance=model)
            inputs = {'form': form_class, 'link': "projects/updated/",'id':request.POST['pk']}
        if (request.POST['obj'] == "application"):
            model = Applications.objects.get(pk=request.POST['pk'])
            form_class = ApplicationsForm(instance=model)
            inputs = {'form': form_class, 'link': "applications/updated/",'id':request.POST['pk']}
        if (request.POST['obj'] == "user"):
            model = Users.objects.get(pk=request.POST['pk'])
            form_class = UsersForm(instance=model)
            inputs = {'form': form_class, 'link': "users/updated/",'id':request.POST['pk']}
        if (request.POST['obj'] == "component"):
            model = Components.objects.get(pk=request.POST['pk'])
            form_class = ComponentsForm(instance=model)
            inputs = {'form': form_class, 'link': "components/updated/",'id':request.POST['pk']}
        if (request.POST['obj'] == "device"):
            model = Devices.objects.get(pk=request.POST['pk'])
            form_class = DevicesForm(instance=model)
            inputs = {'form': form_class, 'link': "devices/updated/",'id':request.POST['pk']}
        if (request.POST['obj'] == "microservice"):
            model = Microservices.objects.get(pk=request.POST['pk'])
            form_class = MicroservicesForm(instance=model)
            inputs = {'form': form_class, 'link': "microservices/updated/",'id':request.POST['pk']}
        if (request.POST['obj'] == "data"):
            model = Data.objects.get(pk=request.POST['pk'])
            form_class = DataForm(instance=model)
            inputs = {'form': form_class, 'link': "data/updated/",'id':request.POST['pk']}

        return render(request, 'IMSMAPPS/dataupdate.html', inputs)


def appsbuilding(request):
    if request.method == 'POST':
        print("kkkkkkkkkkkkkkkkkkkkkk " + request.POST['id'])
        inputs = {'project': list(Projects.objects.values()),
                  'components': list(Components.objects.values()),
                  'devices': list(Devices.objects.values()),
                  'microservices': list(Microservices.objects.values()),
                  'data': list(Data.objects.values()),
                  'option': "data"}
    return render(request, 'IMSMAPPS/builder.html',inputs)
    #return HttpResponse("start building application with id : " + str(request.POST['id']))
def user_login(request):
    def authenticate(email=None, password=None):
        """ Authenticate a user based on email address as the user name. """
        try:
            user = Users.objects.get(email=email,password=password)
            if user.password==password:
                return user
        except Users.DoesNotExist:
            return None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        print(user)
        if user:
            request.session['username']=user.firstname+" "+user.lastname
            request.session['avatar']=str(user.avatar)
            request.session['user_id']=str(user.u_id)
            request.session['address']=user.address
            request.session['type']=user.type

            return HttpResponseRedirect(reverse('index'))

        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(email, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'IMSMAPPS/dataregiser.html', {})
def logout(request):
    print('ddddddddddddd')

    del request.session['username']
    del request.session['avatar']
    del request.session['user_id']
    del request.session['address']
    del request.session['type']

    return HttpResponseRedirect(reverse('index'))
def get_apps(request):
    if(request.method=='POST'):
        options=[]
        data= Applications.objects.filter(project=request.POST.get("project_id"))
        for i in data:
            options.append({'app_id':i.a_id,'name':i.name})

    return JsonResponse((options),safe=False)
def runtime(request):
    code=request.POST.get('code')
    print((code))
    exec(code)
    data={'data':code+" running ... plz wait :)"}

    return render(request,'IMSMAPPS/myapp.html',data)
def pymicroservice(*argv, **kwargs):
    print("run service : "+str(argv[0])+' with option : '+str(kwargs['args']))
ssoijzzuju
def storage(request):
    data={'data':request}
    print(request.encoding)
    return HttpResponse(data)