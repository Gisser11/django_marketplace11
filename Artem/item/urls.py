from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('<int:PRIMARY_KEY>/', views.detail, name='detail')
]