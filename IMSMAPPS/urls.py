from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

#from . import api_del
from . import views
"""
router = routers.DefaultRouter()
router.register(r'projects', api_del.ProjectsViewSet)
router.register(r'applications', api_del.ApplicationsViewSet)
router.register(r'users', api_del.UsersViewSet)
router.register(r'components', api_del.ComponentsViewSet)
router.register(r'devices', api_del.DevicesViewSet)
router.register(r'microservices', api_del.MicroservicesViewSet)
router.register(r'data', api_del.DataViewSet)
"""

urlpatterns = (
    # urls for Django Rest Framework API
   # path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Projects
    path('projects/', views.showadata, name='IMSMAPPS_projects_list'),
    path('projects/create/', views.dataregister, name='IMSMAPPS_projects_create'),
    path('projects/created/', views.datasave, name='IMSMAPPS_projects_create'),
    path('projects/updated/', views.dataresave, name='IMSMAPPS_projects_create'),
#    path('projects/detail/<pk>/', views.ProjectsDetailView.as_view(), name='IMSMAPPS_projects_detail'),
    path('projects/update/', views.dataupdate, name='IMSMAPPS_projects_update'),
    path('projects/delete/', views.datadelete, name='IMSMAPPS_projects_update'),
)

urlpatterns += (
    # urls for Applications
    path('applications/', views.showadata, name='IMSMAPPS_applications_list'),
    path('applications/create/', views.dataregister, name='IMSMAPPS_applications_create'),
    path('applications/created/', views.datasave, name='IMSMAPPS_applications_create'),
    path('applications/updated/', views.dataresave, name='IMSMAPPS_applications_create'),
 #   path('applications/detail/<pk>/', views.ApplicationsDetailView.as_view(), name='IMSMAPPS_applications_detail'),
    path('applications/update/', views.dataupdate, name='IMSMAPPS_applications_update'),
    path('applications/delete/', views.datadelete, name='IMSMAPPS_projects_update'),
    path('applications/building/', views.appsbuilding, name='IMSMAPPS_application_building'),
)

urlpatterns += (
    # urls for Users
    path('users/', views.showadata, name='IMSMAPPS_users_list'),
    path('users/create/', views.dataregister, name='IMSMAPPS_users_create'),
    path('users/created/', views.datasave, name='IMSMAPPS_users_create'),
    path('users/updated/', views.dataresave, name='IMSMAPPS_users_create'),
    path('users/delete/', views.datadelete, name='IMSMAPPS_projects_update'),

  #  path('users/detail/<pk>/', views.UsersDetailView.as_view(), name='IMSMAPPS_users_detail'),
    path('users/update/', views.dataupdate, name='IMSMAPPS_users_update'),
)

urlpatterns += (
    # urls for Components
    path('components/', views.showadata, name='IMSMAPPS_components_list'),
    path('components/create/', views.dataregister, name='IMSMAPPS_components_create'),
    path('components/created/', views.datasave, name='IMSMAPPS_components_create'),
    path('components/updated/', views.dataresave, name='IMSMAPPS_components_create'),
  #  path('components/detail/<pk>/', views.ComponentsDetailView.as_view(), name='IMSMAPPS_components_detail'),
   # path('components/delete/<pk>/', views.ComponentsDetailView.as_view(), name='IMSMAPPS_components_detail'),
    path('components/update/', views.dataupdate, name='IMSMAPPS_components_update'),
    path('components/delete/', views.datadelete, name='IMSMAPPS_projects_update'),
)

urlpatterns += (
    # urls for Devices
    path('devices/', views.showadata, name='IMSMAPPS_devices_list'),
    path('devices/create/', views.dataregister, name='IMSMAPPS_devices_create'),
    path('devices/created/', views.datasave, name='IMSMAPPS_devices_create'),
    path('devices/updated/', views.dataresave, name='IMSMAPPS_devices_create'),
   # path('devices/detail/<pk>/', views.DevicesDetailView.as_view(), name='IMSMAPPS_devices_detail'),
    path('devices/update/', views.dataupdate, name='IMSMAPPS_devices_update'),
    path('devices/delete/', views.datadelete, name='IMSMAPPS_projects_update'),
)

urlpatterns += (
    # urls for Microservices
    path('microservices/', views.showadata, name='IMSMAPPS_microservices_list'),
    path('microservices/create/', views.dataregister, name='IMSMAPPS_microservices_create'),
    path('microservices/created/', views.datasave, name='IMSMAPPS_microservices_create'),
    path('microservices/updated/', views.dataresave, name='IMSMAPPS_microservices_create'),
  #  path('microservices/detail/<pk>/', views.MicroservicesDetailView.as_view(), name='IMSMAPPS_microservices_detail'),
    path('microservices/update/', views.dataupdate, name='IMSMAPPS_microservices_update'),
    path('microservice/delete/', views.datadelete, name='IMSMAPPS_projects_update'),
)

urlpatterns += (
    # urls for Data
    path('data/', views.showadata, name='IMSMAPPS_data_list'),
    path('data/create/', views.dataregister, name='IMSMAPPS_data_create'),
    path('data/created/', views.datasave, name='IMSMAPPS_data_create'),
    path('data/updated/', views.dataresave, name='IMSMAPPS_data_create'),
  #  path('data/detail/<pk>/', views.DataDetailView.as_view(), name='IMSMAPPS_data_detail'),
    path('data/update/', views.dataupdate, name='IMSMAPPS_data_update'),
    path('data/delete/', views.datadelete, name='IMSMAPPS_projects_update'),
)
urlpatterns += (
    url(r'^$', views.index.as_view(), name='index'),
    path('login/', views.login.as_view(), name='login'),
    path('user/login/', views.user_login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('apps/', views.apps.as_view(), name='apps'),

)
