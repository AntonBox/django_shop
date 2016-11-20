from django.views.generic.base import TemplateView
from apps.testview.models import Visual
from django.shortcuts import render_to_response


class TestView(TemplateView):
    template_name = "index.html"


def vision(request):
    visuals = Visual.objects.order_by('index').all()
    return render_to_response('vision.html', {'visuals': visuals})
