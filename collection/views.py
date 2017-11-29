from django.shortcuts import render
from collection.models import Thing
# Create your views here.

def index(request):
	# defining the variable
	things = Thing.objects.all()
	# passing the variable to the view
	return render(request, 'index.html', {
		'things': things,
		 })

def thing_detail(request, slug):
	# grab the object 
	thing = Thing.objects.get(slug=slug)
	# and pass to the template
	return render(request, 'things/thing_detail.html', {
		'thing': thing,
		})