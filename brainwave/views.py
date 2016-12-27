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

def choice(request):
    content = { 'title': '選擇影片類型' }
    return render(request, 'choice.html', content)

def create_qrcode(request):
    content = { 'title': '開始測量' }
    type = request.POST.getlist('type')
    # TODO: Create Qrcode and send the youtube
    return render(request, 'measuring.html', content)
