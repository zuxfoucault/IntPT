from django.shortcuts import render, get_object_or_404

# Create your views here.
from ipts.models import Clinic, Choice
from django.http import HttpResponse, HttpResponseRedirect
#from django.template import Context, loader
#from django.http import Http404
from django.core.urlresolvers import reverse

def index(request):
	clinicList = Clinic.objects.all()
	#output = ', '.join([c.cname for c in clinicList])
	#return HttpResponse(output)
	#template = loader.get_template('ipts/index.html')
	#context = Context({
	#	'clinicList' : clinicList,
	#})
	#return HttpResponse(template.render(context))
	context = {'clinicList' : clinicList}
	return render(request, 'ipts/index.html', context)

def detail(request, pk):
	#return HttpResponse("You're looking at clinic %s." %pk)
	#try:
	#	clinic = Clinic.objects.get(pk=pk)
	#except Clinic.DoesNotExist:
	#	raise Http404
	clinic = get_object_or_404(Clinic, pk=pk)
	return render(request, 'ipts/detail.html', {'clinic':clinic})

def results(request, pk):
	#return HttpResponse("You're looking at results of clinic chosen.")
	clinicList = Clinic.objects.all()
	clinic = get_object_or_404(Clinic, pk=pk)
	return render(request, 'ipts/results.html', {
		'clinic':clinic,
		'clinicList':clinicList,
	})

def chosen(request, pk):
	#return HttpResponse("You're choosing the %s." %pk)
	c = get_object_or_404(Clinic, pk=pk)
	d = c.choice_set.all()
	for choice in d:
		choice.chosen = False
		choice.save()
	try:
		selectedChoice = c.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'ipts/detail.html', {
			'clinic':c,
			'error_message': "You didn't select a choice.",
		})
	else:
		selectedChoice.chosen = True
		selectedChoice.save()
		return HttpResponseRedirect(reverse('ipts:results', args=(c.id,)))

def resultsAll(request):
	clinicList = Clinic.objects.all()
	return render(request, 'ipts/resultsAll.html', {
		'clinicList':clinicList,
	})
