from pydoc import visiblename
from django.http import HttpResponse
from django.template.loader import render_to_string
from dj.models import *

def hello(request):
    tagline_list = Tagline.objects.filter(visible=1)
    menu_items = MenuItem.objects.filter(visible=1)
    return HttpResponse(render_to_string('index.html', {'tags': tagline_list, 'links': menu_items}))