import random
import json
import qrcode
import qrcode.image.svg

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from .extra.analysis_wave import AnalysisWave

aw = AnalysisWave()

def index(request):
    template = loader.get_template('index.html')
    context = {
        'text': 'text'
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def analysis(request, serial_num):
    print(f'analysis:{serial_num}')
    if request.method == 'POST':
        raw_json = json.loads(request.body)
        print(raw_json)
        aw.analysis(serial_num, raw_json['rawData'])
        return JsonResponse({serial_num: 'OK'})
    else:
        content = { 'title': '結果' }
        # TODO: put result
        try:
            content['data'] = aw.wave_result[serial_num]
            return render(request, 'result.html', content)
        except KeyError:
            return render(request, 'opps.html')

def choice(request):
    content = { 'title': '選擇影片類型' }
    return render(request, 'choice.html', content)

def create_qrcode(request):
    content = { 'title': '開始測量' }
    serial_num = random.randrange(10000, 99999)
    # TODO: send the youtube
    factory = qrcode.image.svg.SvgFragmentImage
    svg = qrcode.make(serial_num, image_factory=factory)
    svg.save(f'brainwave/static/qr_code_svg/{serial_num}.svg')

    content['tube_ids'] = request.POST.getlist('type')
    content['svg_path'] = f'qr_code_svg/{serial_num}.svg'
    content['result_path'] = f'/analysis/{serial_num}'

    return render(request, 'measuring.html', content)
