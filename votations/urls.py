"""votations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from main.views import *
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
#from main.models import Acta
from rest_framework import routers, serializers, viewsets
#from votations.modelserializer import ActaSerializer
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken import views
from main.views import *


# class ActaViewSet(viewsets.ModelViewSet):
#     queryset = Acta.objects.all()
#     serializer_class = ActaSerializer

router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)
#router.register(r'Actas', ActaViewSet)
app_name = 'main'
urlpatterns = [
    path('',home.as_view(),name='home'),
    path('estadistica/',estadistica.as_view(),name='estadistica'),
    path('estadistica/filtrar', filtrar,name='estadistica-filtrar'),
    path('admin/', admin.site.urls),
    path('api/models/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),

    path('candidato/crear',CandidatoCreate.as_view(),name='candidato-add'),
    path('candidato/listar', CandidatoList.as_view(), name='candidato-list'),
    path('candidato/editar/<slug:pk>/',CandidatoUpdate.as_view(),name='candidato-update'),
    path('candidato/borrar/<slug:pk>/',CandidatoDelete.as_view(),name='candidato-delete'),

    path('candidatos/buscar', filtrar_candidatos,name='candidatos-buscar'),

    ##GUARDAR ELECCIONES
    path('votos/guardar', guardar_acta_escrutinio,name='escrutinio-guardar'),

    #path('acta/cambiarestado', cambiar_estado,name='acta-cambiar'),

    #path('acta/crear/<slug:pk>/',ActaCreate.as_view(),name='acta-add'),
    #path('acta/listar', ActaList.as_view(), name='acta-list'),
    #path('documentos/listar', TblDocumentList.as_view(), name='documento-list'),

    #path('documentosproceso/listar', ListProceso.as_view(), name='list-proceso'),

    path('escrutinio/crear/',EscrutinioCreate.as_view(),name='escrutinio-add'),
    path('escrutinio/listar', EscrutinioList.as_view(), name='escrutinio-list'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('escrutinio/<slug:pk>/', EscrutinioDetailView.as_view(), name='escrutinio-detail'),

    path('mesa/crear/',MesaCreate.as_view(),name='mesa-add'),
    path('mesa/listar', MesaList.as_view(), name='mesa-list'),

    path('colaborador/crear',ColaboradorCreate.as_view(),name='colaborador-add'),
    path('colaborador/editar/<slug:pk>/',ColaboradorUpdate.as_view(),name='colaborador-update'),
    path('votosg/imprimir/',votos_general ,name='votos-imprimir'),

    #REPORTE
    #path('reporte/escrutinio/',ReporteEscrutiniosExcel.as_view() ,name='escrutinios-excel'),
    url(r'^reporte/escrutinio/$',ReporteEscrutiniosExcel.as_view(), name="escrutinios-excel"),
    #url(r'^reporte_personas_excel/$',ReportePersonasExcel.as_view(), name="reporte_personas_excel"),
    #path('certificado/imprimir/(?P<alumno>\w{0,50})/(?P<grado>\w{0,50})/$',reporte_compras ,name='alumno-imprimir'),
    path('dashboard/', dashboard_with_pivot, name='dashboard_with_pivot'),
    path('data', pivot_data, name='pivot_data'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
