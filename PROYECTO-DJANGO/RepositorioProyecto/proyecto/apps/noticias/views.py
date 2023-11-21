from django.shortcuts import render

# Create your views here.

def Home_Noticias(request):

	return render(request, 'noticias/home_noticias.html')