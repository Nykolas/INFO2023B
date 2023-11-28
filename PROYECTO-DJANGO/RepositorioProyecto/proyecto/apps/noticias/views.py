from django.shortcuts import render
from django.views.generic import ListView


from .models import Noticia

#Vasta Basada en funciones
def Home_Noticias(request):

	#ORM
	todas = Noticia.objects.all()

	contexto = {}

	contexto['noticias'] = todas
	contexto['fecha'] = '28-11-2023'

	return render(request, 'noticias/home_noticias.html', contexto)

#ACLARACION
'''
si bien en la vista armo un diccionario del tipo
{noticias: todas_noticias, fecha: '28-11-2023'}
en el template resivo variables separadas, una por cada clave, la cual contiene como valor
el valor de la clave
EJ, recibo 2 variales distintas, cuyo nombre es igual a la clave
noticias = todas_noticias
fecha = '28-11-2023'
'''

#VISTA BASADA EN CLASE
class Home_Noticias_clase(ListView):
	model = Noticia
	template_name = 'noticias/home_noticias.html'
	context_object_name = 'noticias'


#ORM
# CONSULTA PARA TRAER TODOS LOS DATOS
# select * from Noticia  SQL
# Noticia.objects.all()   ORM

#CONSuLTA PARA TRAER SOLO UN DATO (POR CLAVE)
# select * from Noticia where id = algo    SQL
# Noticia.objects.get(id = algo)		ORM

#CONSuLTA PARA TRAER SOLO Algunos datos (POR filtro)
# select * from Noticia where categororia = deportes
# Noticia.objects.filter(categoria = deportes)