from django.shortcuts import render, redirect
from django.views import View

from .models import Name


# Create your views here.

class Index(View):
    model = Name.objects.all()

    def get(self, request):
        return render(request, 'veni/index.html')


class MakeData(View):

    def get(self, request):
        return render(request, 'veni/index.html')

    def post(self, request, *args, **kwargs):
        data = request.POST
        print(data)
        n = Name.objects.create(data=data)
        n.save()
        print(n)

        return redirect('show')


class Show(View):
    def get(self, request):
        data = Name.objects.all()
        data = list(data)

        return render(request, 'veni/show.html', context={'data': data})
