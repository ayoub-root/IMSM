import uuid
import time
from importlib import import_module

from django import forms
from django.contrib.messages.storage import session
from django.http import request

from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.db import models as models
#from requests import Session
from django.contrib.sessions.models import Session

from IMSM import settings


def upld(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        return 'uploads/background/{}.{}'.format(instance.pk, ext)
    else:
        pass
class Users(models.Model):
    # Fields
    u_id = models.CharField(primary_key=True, max_length=100, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    address = models.TextField(max_length=1024)
    birthday = models.DateField()
    avatar = models.FileField(upload_to="uploads/users/",blank=True, null=True)
    type = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.email
    def __unicode__(self):
        return u'%s' % self.u_id

    def get_absolute_url(self):
        print(self.u_id)
        return reverse('IMSMAPPS_users_detail', args=(self.u_id,))

    def get_update_url(self):
        return reverse('IMSMAPPS_users_update', args=(self.u_id,))


class Projects(models.Model):
    # Fields
    p_id = models.CharField(primary_key=True, max_length=100, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,unique=True)
    description = models.TextField(max_length=1024)
    background = models.FileField(upload_to=upld)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    userid = models.ForeignKey(
        'IMSMAPPS.Users',
        on_delete=models.CASCADE, related_name="projects",
        default=Session.session_data



    )

    class Meta:
        ordering = ('-created',)


    def __str__(self):
        return self.name
    def __unicode__(self):
        return u'%s' % self.p_id

    def get_absolute_url(self):
        return reverse('IMSMAPPS_projects_detail', args=(self.p_id,))

    def get_update_url(self):
        return reverse('IMSMAPPS_projects_update', args=(self.p_id,))


class Applications(models.Model):
    # Fields
    a_id = models.CharField(primary_key=True, max_length=100, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1024)
    category = models.CharField(max_length=30)
    background = models.FileField(upload_to=upld)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    userid = models.ForeignKey(
        'IMSMAPPS.Users',
        on_delete=models.CASCADE, related_name="applications",

    )
    project = models.ForeignKey(
        'IMSMAPPS.Projects',
        on_delete=models.CASCADE, related_name="applications",


    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return u'%s' % self.a_id

    def get_absolute_url(self):
        return reverse('IMSMAPPS_applications_detail', args=(self.a_id,))

    def get_update_url(self):
        return reverse('IMSMAPPS_applications_update', args=(self.a_id,))



class Components(models.Model):
    # Fields
    c_id = models.CharField(primary_key=True, max_length=100, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1024)
    background = models.FileField(upload_to=upld,default="avatar")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    # Relationship Fields
    application = models.ForeignKey(
        'IMSMAPPS.Applications',
        on_delete=models.CASCADE, related_name="components",

    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return u'%s' % self.c_id

    def get_absolute_url(self):
        return reverse('IMSMAPPS_components_detail', args=(self.c_id,))

    def get_update_url(self):
        return reverse('IMSMAPPS_components_update', args=(self.c_id,))


class Devices(models.Model):
    # Fields
    d_id = models.CharField(primary_key=True, max_length=100, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1024)
    type = models.CharField(max_length=30)
    background = models.FileField(upload_to=upld,default="avatar")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    component = models.ForeignKey(
        'IMSMAPPS.Components',
        on_delete=models.CASCADE, related_name="devices",
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return u'%s' % self.d_id

    def get_absolute_url(self):
        return reverse('IMSMAPPS_devices_detail', args=(self.d_id,))

    def get_update_url(self):
        return reverse('IMSMAPPS_devices_update', args=(self.d_id,))


class Microservices(models.Model):
    # Fields
    m_id = models.CharField(primary_key=True, max_length=100, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1024)
    url = models.CharField(max_length=255)
    cmd = models.TextField(max_length=1024)
    creator = models.CharField(max_length=255)
    users = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    inputs = models.TextField(max_length=255)
    outputs = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


    # Relationship Fields
    device = models.ForeignKey(
        'IMSMAPPS.Devices',
        on_delete=models.CASCADE, related_name="microservices",
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return u'%s' % self.m_id

    def get_absolute_url(self):
        return reverse('IMSMAPPS_microservices_detail', args=(self.m_id,))

    def get_update_url(self):
        return reverse('IMSMAPPS_microservices_update', args=(self.m_id,))


class Data(models.Model):
    # Fields
    data_id = models.CharField(primary_key=True, max_length=100, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    value = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name
    def __unicode__(self):
        return u'%s' % self.data_id

    def get_absolute_url(self):
        return reverse('IMSMAPPS_data_detail', args=(self.data_id,))

    def get_update_url(self):
        return reverse('IMSMAPPS_data_update', args=(self.data_id,))
