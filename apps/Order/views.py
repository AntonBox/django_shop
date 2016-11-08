from django.views.generic.base import TemplateView
# Create your views here.


class TestView(TemplateView):
    template_name = 'index.html'
