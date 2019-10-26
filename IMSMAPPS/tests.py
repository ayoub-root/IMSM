import unittest
from django.urls import reverse
from django.test import Client
from .models import Projects, Applications, Users, Components, Devices, Microservices, Data
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_projects(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["description"] = "description"
    defaults["background"] = "background"
    defaults.update(**kwargs)
    return Projects.objects.create(**defaults)


def create_applications(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["description"] = "description"
    defaults["category"] = "category"
    defaults["background"] = "background"
    defaults.update(**kwargs)
    return Applications.objects.create(**defaults)


def create_users(**kwargs):
    defaults = {}
    defaults["email"] = "email"
    defaults["firstname"] = "firstname"
    defaults["lastname"] = "lastname"
    defaults["password"] = "password"
    defaults["address"] = "address"
    defaults["birthday"] = "birthday"
    defaults["avatar"] = "avatar"
    defaults["type"] = "type"
    defaults.update(**kwargs)
    return Users.objects.create(**defaults)


def create_components(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["description"] = "description"
    defaults["background"] = "background"
    defaults.update(**kwargs)
    return Components.objects.create(**defaults)


def create_devices(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["description"] = "description"
    defaults["type"] = "type"
    defaults.update(**kwargs)
    return Devices.objects.create(**defaults)


def create_microservices(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["description"] = "description"
    defaults["url"] = "url"
    defaults["cmd"] = "cmd"
    defaults["creator"] = "creator"
    defaults["users"] = "users"
    defaults["category"] = "category"
    defaults["inputs"] = "inputs"
    defaults["outputs"] = "outputs"
    defaults.update(**kwargs)
    return Microservices.objects.create(**defaults)


def create_data(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["type"] = "type"
    defaults["value"] = "value"
    defaults.update(**kwargs)
    return Data.objects.create(**defaults)


class ProjectsViewTest(unittest.TestCase):
    '''
    Tests for Projects
    '''

    def setUp(self):
        self.client = Client()

    def test_list_projects(self):
        url = reverse('IMSMAPPS_projects_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_projects(self):
        url = reverse('IMSMAPPS_projects_create')
        data = {
            "name": "name",
            "description": "description",
            "background": "background",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_projects(self):
        projects = create_projects()
        url = reverse('IMSMAPPS_projects_detail', args=[projects.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_projects(self):
        projects = create_projects()
        data = {
            "name": "name",
            "description": "description",
            "background": "background",
        }
        url = reverse('IMSMAPPS_projects_update', args=[projects.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ApplicationsViewTest(unittest.TestCase):
    '''
    Tests for Applications
    '''

    def setUp(self):
        self.client = Client()

    def test_list_applications(self):
        url = reverse('IMSMAPPS_applications_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_applications(self):
        url = reverse('IMSMAPPS_applications_create')
        data = {
            "name": "name",
            "description": "description",
            "category": "category",
            "background": "background",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_applications(self):
        applications = create_applications()
        url = reverse('IMSMAPPS_applications_detail', args=[applications.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_applications(self):
        applications = create_applications()
        data = {
            "name": "name",
            "description": "description",
            "category": "category",
            "background": "background",
        }
        url = reverse('IMSMAPPS_applications_update', args=[applications.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class UsersViewTest(unittest.TestCase):
    '''
    Tests for Users
    '''

    def setUp(self):
        self.client = Client()

    def test_list_users(self):
        url = reverse('IMSMAPPS_users_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_users(self):
        url = reverse('IMSMAPPS_users_create')
        data = {
            "email": "email",
            "firstname": "firstname",
            "lastname": "lastname",
            "password": "password",
            "address": "address",
            "birthday": "birthday",
            "avatar": "avatar",
            "type": "type",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_users(self):
        users = create_users()
        url = reverse('IMSMAPPS_users_detail', args=[users.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_users(self):
        users = create_users()
        data = {
            "email": "email",
            "firstname": "firstname",
            "lastname": "lastname",
            "password": "password",
            "address": "address",
            "birthday": "birthday",
            "avatar": "avatar",
            "type": "type",
        }
        url = reverse('IMSMAPPS_users_update', args=[users.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ComponentsViewTest(unittest.TestCase):
    '''
    Tests for Components
    '''

    def setUp(self):
        self.client = Client()

    def test_list_components(self):
        url = reverse('IMSMAPPS_components_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_components(self):
        url = reverse('IMSMAPPS_components_create')
        data = {
            "name": "name",
            "description": "description",
            "background": "background",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_components(self):
        components = create_components()
        url = reverse('IMSMAPPS_components_detail', args=[components.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_components(self):
        components = create_components()
        data = {
            "name": "name",
            "description": "description",
            "background": "background",
        }
        url = reverse('IMSMAPPS_components_update', args=[components.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DevicesViewTest(unittest.TestCase):
    '''
    Tests for Devices
    '''

    def setUp(self):
        self.client = Client()

    def test_list_devices(self):
        url = reverse('IMSMAPPS_devices_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_devices(self):
        url = reverse('IMSMAPPS_devices_create')
        data = {
            "name": "name",
            "description": "description",
            "type": "type",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_devices(self):
        devices = create_devices()
        url = reverse('IMSMAPPS_devices_detail', args=[devices.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_devices(self):
        devices = create_devices()
        data = {
            "name": "name",
            "description": "description",
            "type": "type",
        }
        url = reverse('IMSMAPPS_devices_update', args=[devices.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class MicroservicesViewTest(unittest.TestCase):
    '''
    Tests for Microservices
    '''

    def setUp(self):
        self.client = Client()

    def test_list_microservices(self):
        url = reverse('IMSMAPPS_microservices_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_microservices(self):
        url = reverse('IMSMAPPS_microservices_create')
        data = {
            "name": "name",
            "description": "description",
            "url": "url",
            "cmd": "cmd",
            "creator": "creator",
            "users": "users",
            "category": "category",
            "inputs": "inputs",
            "outputs": "outputs",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_microservices(self):
        microservices = create_microservices()
        url = reverse('IMSMAPPS_microservices_detail', args=[microservices.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_microservices(self):
        microservices = create_microservices()
        data = {
            "name": "name",
            "description": "description",
            "url": "url",
            "cmd": "cmd",
            "creator": "creator",
            "users": "users",
            "category": "category",
            "inputs": "inputs",
            "outputs": "outputs",
        }
        url = reverse('IMSMAPPS_microservices_update', args=[microservices.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DataViewTest(unittest.TestCase):
    '''
    Tests for Data
    '''

    def setUp(self):
        self.client = Client()

    def test_list_data(self):
        url = reverse('IMSMAPPS_data_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_data(self):
        url = reverse('IMSMAPPS_data_create')
        data = {
            "name": "name",
            "type": "type",
            "value": "value",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_data(self):
        data = create_data()
        url = reverse('IMSMAPPS_data_detail', args=[data.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_data(self):
        data = create_data()
        data = {
            "name": "name",
            "type": "type",
            "value": "value",
        }
        url = reverse('IMSMAPPS_data_update', args=[data.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
