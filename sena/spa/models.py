from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    foto = models.CharField(max_length=20) # Cambio a ImageField() mas adelante
    ROLES = (
        (1, 'Administrador'),
        (2, 'Profesional'),
        (3, 'Secretari@'),
        (4, 'Cliente'),
    )
    rol = models.IntegerField(choices=ROLES, default=4)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Servicio(models.Model):
    nombre = models.CharField(max_length=254)
    costo = models.IntegerField()
    descripcion = models.TextField(null=True, blank=True)
    ESTADOS = (
        ('Activo', 'ACTIVO'),
        ('Inactivo', 'INACTIVO'),
    )
    estado = models.CharField(max_length=8, choices=ESTADOS, default='Activo')

    def __str__(self):
        return f'Nombre: {self.nombre} / Costo: $ {self.costo}'

class Cita(models.Model):
    cliente = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING, related_name='fk1_cita_usuario_cliente')
    profesional = models.ForeignKey('Usuario', on_delete=models.DO_NOTHING, related_name='fk2_cita_usuario_profesional')
    servicio = models.ForeignKey('Servicio', on_delete=models.DO_NOTHING)
    fecha_cita = models.DateTimeField(help_text='AAAA-MM-DD')
    ESTADOS = (
        ('R', 'Reservada'),
        ('C', 'Cancelada'),
        ('A', 'Atendida'),
    )
    estado = models.CharField(max_length=1, choices=ESTADOS, default='R')

    def __str__(self):
        return f'''Cliente: {self.cliente}. / 
        Profesional: {self.profesional}. / 
        Servicio: {self.servicio} / 
        Costo: $ {self.servicio.costo} / 
        Fecha: {self.fecha_cita}'''