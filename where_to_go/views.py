from django.http import HttpResponse
from django.template import loader


def index_page(request):
    context = {}
    template = loader.get_template('index.html')
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)