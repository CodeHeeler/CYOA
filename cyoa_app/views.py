from django.shortcuts import render
from django.http import HttpResponse
from .models import Page, Choice


def page(request, page_id):
    context = {}
    print(page_id)
    context['page'] = Page.objects.get(id=page_id)
    context['choices'] = Choice.objects.filter(from_page_id=page_id)
    return render(request, 'cyoa/page.html', context)
