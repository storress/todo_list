from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addTask$', views.addTask, name = 'addTask'),
    url(r'^deleteTask$', views.TaskDelete.asView, name = 'delete'),
    ]