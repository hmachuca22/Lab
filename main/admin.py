from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *
#Candidato,Departamento,Municipio,Aldea,Corriente, Tipo, CentroEducativo
#Acta
from import_export.admin import ImportExportModelAdmin

class MesaAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Mesa, MesaAdmin)

class ColaboradorAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Colaborador, ColaboradorAdmin)


class PartidoAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Partido, PartidoAdmin)

class CandidatoAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Candidato, CandidatoAdmin)

class CentroAdmin(ImportExportModelAdmin):
    pass

admin.site.register(CentroEducativo, CentroAdmin)

class TipoAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Tipo, TipoAdmin)

class DepartamentoAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Departamento, DepartamentoAdmin)


class MunicipioAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Municipio, MunicipioAdmin)


class AldeaAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Aldea, AldeaAdmin)

#
# class ActaAdmin(ImportExportModelAdmin):
#     pass
#
# admin.site.register(Acta, ActaAdmin)

class CorrienteAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Corriente, CorrienteAdmin)
