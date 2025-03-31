from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("inicio/", views.inicio, name="inicio"),
    path("saludar/<str:nombre>/<str:apellido>/",views.saludar, name="saludar"),
    path("calculadora/<int:n1>/<int:n2>/<str:operador>/", views.calculadora, name="calculadora"),
    path("cuadrado_formulario/", views.cuadrado_formulario, name="cuadrado_formulario"),
    path('calc/', views.calc, name='calc'),

    # CRUD servicios
    path('servicios/', views.servicios, name='servicios'), #    ver
    path('eliminar_servicio/<int:id_servicio>/', views.eliminar_servicio, name='eliminar_servicio'), #  eliminar

    # CRUD usuarios
    path('usuarios/', views.usuarios, name='usuarios'),

    # correos
    path('correos1/', views.correos1, name='correos1'),
    path('correos2/', views.correos2, name='correos2'),
    # path('correos3/', views.correos3, name='correos3'),

    # cambio contraseña
    path('cambiar_clave/', views.cambiar_clave, name='cambiar_clave'),
]
