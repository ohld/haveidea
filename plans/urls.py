from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('latest/', views.latest, name='latest'),
    path('top/', views.top, name='top'),
    path('<int:plan_id>/', views.detail, name='detail'),
]