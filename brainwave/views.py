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

YOUTUBE_TABLE = {
    '1': '//www.youtube.com/embed/h1J1gRw6cRc',
    '2': '//www.youtube.com/embed/10ug1iSb074',
    '3': '//www.youtube.com/embed/F6qX4HSWMTM',
    '4': '//www.youtube.com/embed/AUKu_90PfHk',
    '5': '//www.youtube.com/embed/JvbNt8iq6QQ',
    '6': '//www.youtube.com/embed/UlWAGSgJfq0'
}

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
        aw.analysis(serial_num, raw_json)
        return JsonResponse({serial_num: 'OK'})
    else:
        content = { 'title': '結果' }
        try:
            content['x_label'] = aw.get_times(serial_num)
            content['a_data'] = aw.get_wave(serial_num, 0)
            content['b_data'] = aw.get_wave(serial_num, 1)
            content['y_data'] = aw.get_wave(serial_num, 2)
            content['match'] = ["喜劇", "恐怖"]
            content['unmatch'] = ["動畫", "科幻"]
            return render(request, 'result.html', content)
        except KeyError:
            return render(request, 'opps.html')

def choice(request):
    content = { 'title': '選擇影片類型' }
    return render(request, 'choice.html', content)

def create_qrcode(request):
    content = { 'title': '開始測量', 'youtube_links': [] }
    serial_num = random.randrange(10000, 99999)

    factory = qrcode.image.svg.SvgFragmentImage
    svg = qrcode.make(serial_num, image_factory=factory)
    svg.save(f'brainwave/static/qr_code_svg/{serial_num}.svg')

    youtube_ids = request.POST.getlist('type')
    for id in youtube_ids:
        content['youtube_links'].append(YOUTUBE_TABLE[id])

    content['svg_path'] = f'qr_code_svg/{serial_num}.svg'
    content['result_path'] = f'/analysis/{serial_num}'

    return render(request, 'measuring.html', content)
