from django.urls import path, include
from . import views
from django.contrib.auth.views import login_required

urlpatterns = [

    # localhost:8000/listarCarreras 
    path('listarCarreras', views.listar_carreras,name="listar_carreras"),
    
    # localhost:8000/agregar_carrera
    path('agregar_carrera', views.agregar_carrera, name="agregar_carrera"),

    # # editar una carrera
    # path('editar_carrera/<int:carrera_id>', views.editar_carrera ,name="editar_carrera"),

    # # borrar una carrera
    # path('borrar_carrera/<int:carrera_id>', views.borrar_carrera, name="borrar_carrera"),
    # editar una carrera
    path('editar_carrera/<int:carrera_id>', login_required(views.editar_carrera), name="editar_carrera"),

    # borrar una carrera
    path('borrar_carrera/<int:carrera_id>', login_required(views.borrar_carrera), name="borrar_carrera"),



    # LLAMAMOS A LOS GENERICS
    path('add_carrera', views.CarreraCreate.as_view(), name="add_carrera"),
    
    
    path('list_carrera', views.CarreraList.as_view(), name="list_carreras"),
    
    # ELIMINAR CON GENERICS
    path('del_carrera/<pk>', views.CarreraDelete.as_view(), name="del_carrera"),
    
    # ELIMINAR CON GENERICS
    path('update_carrera/<pk>', views.CarreraUpdate.as_view(), name="update_carrera"),
    
    
]
