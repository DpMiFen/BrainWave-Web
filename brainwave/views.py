from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {
        'text': 'text'
    }
    return HttpResponse(template.render(context, request))

def result(request):
    return render(request, 'result.html')