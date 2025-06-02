from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('registrar/', views.registro_usuario, name='registro_usuario'),
    path('inicar/', views.login_usuario, name='login_usuario'),
    path('menu/', views.menu_principal, name='menu_principal')

]