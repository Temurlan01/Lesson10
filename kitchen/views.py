from django.shortcuts import render
from django.views.generic import TemplateView
from kitchen.models import Sushis


class PizzaListTemplateView(TemplateView):
    template_name = 'pizza_list.html'


class SushiListView(TemplateView):
    template_name = 'Sushi_list.html'

    def get_context_data(self, **kwargs):
        context = dict()
        sushis = Sushis.objects.first()
        context['first_sushi'] = sushis
        return context


