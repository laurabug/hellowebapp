from django.shortcuts import render, redirect
from collection.forms	import ThingForm
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

def edit_thing(request, slug):
	# grab the object 
	thing = Thing.objects.get(slug=slug)
	# set the form we are using
	form_class = ThingForm
	# if we are coming to this view from a submitted form,
	if request.method == 'POST':
		# grab the data from the submitted from
		form = form_class(data=request.POST, instance=thing)
		if form.is_valid():
			#save the new data
			form.save()
			return redirect('thing_detail', slug=thing.slug)
	# otherwise just create the form
	else:
		form = form_class(instance=thing)
	# and render the template
	return render(request, 'things/edit_thing.html', {
		'thing': thing,
		'form': form,
		})