from django.urls import re_path
from webapi.tipo_auto.view import tipo_auto_list, tipo_auto_marca_list
from webapi.color.view import color_list, color_detail
from webapi.genero.view import genero_list
from webapi.cliente.view import cliente_list, cliente_detail
from webapi.auto.view import auto_list, auto_detail
from webapi.auto.view import auto_colores, auto_colores_detail
from webapi.marca.view import marca_list






urlpatterns = [
      re_path(r'^api/tipo_autos$', tipo_auto_list )
    , re_path(r'^api/tipo:autos/(?P<id>\d+)$', tipo_auto_detail )
    , re_path(r'^api/tipo_autos/(?P<id>\d+)', tipo_auto_marca_list)
    
    , re_path(r'^api/colores$', color_list )
    , re_path(r'^api/colores/(?P<id>\d+)$', color_detail )
    , re_path(r'^api/generos$', genero_list )

    , re_path(r'^api/clientes$', cliente_list )
    , re_path(r'^api/clientes/(?P<id>\d+)$', cliente_detail )

    , re_path(r'^api/autos$', auto_list )
    , re_path(r'^api/autos/(?P<id>\d+)$', auto_detail )
    , re_path(r'^api/autos/(?P<id>\d+)/colores$', auto_colores )
    , re_path(r'^api/autos/(?P<id>\d+)/colores/(?P<id_color>\d+)$', auto_colores_detail )

    , re_path(r'^api/marca$', marca_list)
    , re_path(r'^api/marca/(?P<id>\d+)$', marca_detail )
    , re_path(r'^api/modelo$', modelo_list)
    , re_path(r'^api/modelo/(?P<id>\d+)$', modelo_detail )


]