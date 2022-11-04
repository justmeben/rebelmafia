from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        context = {'rabbit': 'is nice'}
        return render(request, 'index.html', context=context)
