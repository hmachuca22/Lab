from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.
## Mesa
## Acta

class ModeloBase(models.Model):
    created_at =    models.DateTimeField(default=datetime.now(), blank=True)
    user_created =  models.ForeignKey(User,on_delete=models.CASCADE, related_name='%(class)s_requests_user_created')
    update_at =     models.DateTimeField(default=datetime.now(), blank=True)
    user_update =   models.ForeignKey(User,on_delete=models.CASCADE, related_name='%(class)s_requests_user_update')

    class Meta:
        abstract = True

class Departamento(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=150)
    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=150)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    def __str__(self):
        #return self.departamento.nombre + ' | ' +self.nombre
        return self.nombre

class Aldea(ModeloBase):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=150)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Tipo(ModeloBase):
    nombre = models.CharField(max_length=150)
    descripcion  = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Corriente(ModeloBase):
    nombre = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='media/corriente')

    #candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Partido(ModeloBase):
    orden = models.IntegerField(default=1)
    nombre = models.CharField(max_length=40)
    logo = models.ImageField(upload_to='media/corriente')

    def __str__(self):
        return self.nombre

class Candidato(ModeloBase):
    GENDER_CHOICES = [
    ('F', 'Femenino'),
    ('M', 'Masculino'),
]
    departamento = models.ForeignKey(Departamento,related_name='departamento_candidatos', on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    #corriente = models.ManyToManyField(Corriente, related_name='corriente_candidato')
    identidad = models.CharField(max_length=150, null = True)
    nombre = models.CharField(max_length=150)
    Sexo = models.CharField(
        max_length=15,
        choices=GENDER_CHOICES,
    )
    activo = models.BooleanField(default=True)
    casilla = models.IntegerField()
    #telefono = models.CharField(max_length=150)
    #email = models.EmailField(max_length=150,)
    #direccion = models.CharField(max_length=650,)
    foto = models.ImageField(upload_to='media/candidato',max_length=300)
    #grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    #clase = models.ManyToManyField(Clase)

    def __str__(self):
        return self.nombre + " - " +self.partido.nombre


class CentroEducativo(ModeloBase):
    departamento = models.ForeignKey(Departamento,related_name='departamento_centroeducativo', on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio,related_name='municipio_centroeducativo',on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre
        #+ " - " + self.nombre

    def name_short(self):
        return "a"

#
# class Inscripcion(ModeloBase):
#     candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
#     corriente = models.ForeignKey(Corriente, on_delete= models.CASCADE)

class Mesa(ModeloBase):
    centro = models.ForeignKey(CentroEducativo,related_name='CentroEducativo',on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=150,null=True)
    numero = models.CharField(max_length=10)

    def __str__(self):
        return self.numero + " || " + str(self.centro.codigo) + " -- " + self.centro.nombre  + " (" + self.centro.departamento.nombre + " | " + self.centro.municipio.nombre + ")"

    def name_short(self):
        return "a"



#################SISTEMA ########################################
#
# class TblDepartmentsMunicipalities(models.Model):
#     id_distrito = models.AutoField(db_column='ID_DISTRITO', primary_key=True)  # Field name made lowercase.
#     name = models.CharField(db_column='NAME', max_length=1000)  # Field name made lowercase.
#     code_real = models.CharField(db_column='CODE_REAL', unique=True, max_length=4)  # Field name made lowercase.
#     id_depto = models.IntegerField(db_column='ID_DEPTO', blank=True, null=True)  # Field name made lowercase.
#     active = models.SmallIntegerField(db_column='ACTIVE', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'TBL_DEPARTMENTS_MUNICIPALITIES'
#
#
# class TblDocument(models.Model):
#     id_document = models.AutoField(db_column='ID_DOCUMENT', primary_key=True)  # Field name made lowercase.
#     doc_number = models.CharField(db_column='DOC_NUMBER', max_length=1000)  # Field name made lowercase.
#     b64_doc_code = models.TextField(db_column='B64_DOC_CODE')  # Field name made lowercase.
#     tipo_doc = models.TextField(db_column='TIPO_DOC')  # Field name made lowercase.
#     id_person = models.ForeignKey('TblPerson', models.DO_NOTHING, db_column='ID_PERSON')  # Field name made lowercase.
#     latitude = models.CharField(db_column='LATITUDE', max_length=1000)  # Field name made lowercase.
#     longitude = models.CharField(db_column='LONGITUDE', max_length=1000)  # Field name made lowercase.
#     create_date = models.DateField(db_column='CREATE_DATE')  # Field name made lowercase.
#     active = models.SmallIntegerField(db_column='ACTIVE', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'TBL_DOCUMENT'
#
# class TblPerson(models.Model):
#     id_person = models.AutoField(db_column='ID_PERSON', primary_key=True)  # Field name made lowercase.
#     name = models.CharField(db_column='NAME', max_length=500)  # Field name made lowercase.
#     id_number = models.CharField(db_column='ID_NUMBER', max_length=500)  # Field name made lowercase.
#     phone = models.CharField(db_column='PHONE', max_length=9)  # Field name made lowercase.
#     code_depto = models.ForeignKey(TblDepartmentsMunicipalities, models.DO_NOTHING, db_column='CODE_DEPTO', related_name='person_departamento')  # Field name made lowercase.
#     code_municipality = models.ForeignKey(TblDepartmentsMunicipalities, models.DO_NOTHING, db_column='CODE_MUNICIPALITY', related_name = 'persona_municipio')  # Field name made lowercase.
#     create_date = models.DateTimeField(db_column='CREATE_DATE')  # Field name made lowercase.
#     active = models.SmallIntegerField(db_column='ACTIVE', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'TBL_PERSON'
#
#
# class Acta(ModeloBase):
#     documento = models.ForeignKey(TblDocument,related_name='documento_acta', on_delete=models.CASCADE)
#     departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
#     municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE)
#     tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
#     mesa = models.CharField(max_length=64, unique=True)
#     #numero = models.CharField(max_length=150)
#     aldea  = models.CharField(max_length=150, null = True)
#     #origen = models.CharField(max_length=150)
#     descripcion = models.CharField(max_length=150)



class Escrutinio(ModeloBase):
    #TIPOS_CHOICES = [||
    #    ('C', 'Conteo'),
    #    ('VB', 'Votos Blancos'),
    #    ('VN', 'Votos Nulos'),
    #    ('GT', 'Gran Total'),
    #]
    mesa = models.ForeignKey(Mesa,related_name='mesa_votos',on_delete=models.CASCADE)
    #mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE,related_name='mesa_votos',verbose_name="Mesa")
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, null= True)
    valor = models.IntegerField( max_length=15)


class Colaborador(ModeloBase):
    GENDER_CHOICES = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    ]
    USER_CHOICES = [
        ('G', 'GENERAL'),
        ('D', 'DEPARTAMENTAL'),
        ('M', 'MUNICIPAL'),
    ]
    user = models.OneToOneField(User,related_name='colaborador_user', on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, related_name='municipio_usuario',on_delete=models.CASCADE)
    tipo = models.CharField(
        max_length=15,
        choices=USER_CHOICES,
    )
    identidad = models.CharField(max_length=150, null = True)
    nombre = models.CharField(max_length=150)
    sexo = models.CharField(
        max_length=15,
        choices=GENDER_CHOICES,
    )
    foto = models.ImageField(upload_to='media/usuarios',max_length=300)


    def __str__(self):
        return self.user.username + " - - " + self.municipio.nombre


class resumendata(models.Model):
    departamento_id = models.IntegerField()
    departamento = models.CharField(max_length=40)
    municipio_id = models.IntegerField()
    municipio = models.CharField(max_length=40)
    centro_id = models.IntegerField()
    centro = models.CharField(max_length=40)
    mesa_id = models.IntegerField()
    mesa = models.CharField(max_length=40)
    candidato_tipo = models.CharField(max_length=40)
    partido = models.CharField(max_length=40)
    candidato_id = models.IntegerField()
    candidato = models.CharField(max_length=40)
    votos = models.IntegerField()
