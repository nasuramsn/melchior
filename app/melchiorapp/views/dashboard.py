from django.views.generic import View
from django.shortcuts import render
from django.http.response import HttpResponse


class Dashboard(View):
    ''' dashboard screen
    '''

    template_name: str = 'melchior/dashboard/index.html'

    def get(self, request, *args, **kwargs):
        context :dict = {}

        return render(request, self.template_name, context)
