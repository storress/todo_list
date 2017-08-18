from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addTask$', views.addTask, name = 'addTask'),
    url(r'^deleteTask/(?P<task_id>\d+)$', views. deleteTask, name = 'deleteTask'),
    url(r'^completeTask/(?P<task_id>\d+)$', views. completeTask, name = 'completeTask'),
    url(r'^editTask$', views.editTask, name = 'editTask')
    ]