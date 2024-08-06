from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    CONTENT = []

    with open('data-398-2018-08-30.csv', encoding='utf-8') as list:
        full_list = csv.DictReader(list)
        for row in full_list:
            CONTENT.append(row)

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
1