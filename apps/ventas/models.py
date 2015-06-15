from django.db import models

class Cliente(models.Model):
	nombre = models.CharField(max_length=200)
	apellido = models.CharField(max_length=200)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.nombre,self.apellido)
		return nombreCompleto

class Producto(models.Model):
	"""docstring for Producto"""
	nombre = models.CharField(max_length=100)
	dscr = models.TextField(max_length=300)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre



	
		