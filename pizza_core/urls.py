
from django.contrib import admin
from django.urls import path

from kitchen.views import PizzaListTemplateView
from kitchen.views import SushiListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizzas/', PizzaListTemplateView.as_view()),
    path('sushi/', SushiListView.as_view())
]
