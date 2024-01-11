from django.shortcuts import render
from .models import Cards

def index(request):
	context = {
		'cards': Cards.objects.all()
	}
	return render(request,'myapp/index.html',context=context)


def card_id(request,id):
	context = {
		'cards': Cards.objects.filter(id=id)
	}
	return render(request,'myapp/card-id/card-id.html',context=context)

def card_add(request):
	pass
	























