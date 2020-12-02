from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from .models import Data
from django.urls import reverse_lazy
from rest_framework import viewsets
from .serializers import DataSerializer
from .models import Data
from django.http import HttpResponse


import csv
# Create your views here.



class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all().order_by('id')
    serializer_class = DataSerializer

class DataListView(ListView):
    model = Data
    template_name = 'data-list.html'

class DataCreateView(CreateView):
    model = Data
    template_name = 'data-create.html'
    fields = ('temperature', 'relative_humidity', 'barometric_pressure', 'precipitation', 'incoming_solar_radiation', 'outgoing_solar_radiation', 'wind_speed', 'wind_direction', 'photosynthetically_active_radiation', 'captured_sensor_time_date')
    success_url = reverse_lazy('data-list')

class DataDetailView(DetailView):
    model = Data
    template_name = 'data-detail.html'

class DataUpdateView(UpdateView):
    model = Data
    template_name = 'data-update.html'
    fields = ('temperature', 'relative_humidity', 'barometric_pressure', 'precipitation', 'incoming_solar_radiation', 'outgoing_solar_radiation', 'wind_speed', 'wind_direction', 'photosynthetically_active_radiation', 'captured_sensor_time_date')
    success_url = reverse_lazy('data-list')

class DataDeleteView(DeleteView):
    model = Data
    template_name = 'data-delete.html'
    success_url = reverse_lazy('data-list')
def show(request):
    table = Data.objects.all()
    return render(request,"show.html",{'object_list':table})

def graph(request):
    query= Data.objects.all()
    qs = query [len(query) - 5 :]  #last 5 data is plotted)
    return render(request,"chart.html",{'object_list':qs})

def exportcsv(request):
    qs_csv = Data.objects.all()
    response = HttpResponse('')
    response['Content-Disposition'] = 'attachment; filename=qs_csv.csv'
    writer = csv.writer(response)
    writer.writerow(['Log Date Time','Temp_°C', 'R.Hum_%', 'B.Pressure_mbar', 'Precipitation_mm', 'I.S.Rradiation_W/m²', 'O.S.Radiation_W/m²', 'W.Speed_m/s', 'W.Direction', 'P.A.R.'])
    csv_data = qs_csv.values_list('captured_sensor_time_date','temperature', 'relative_humidity', 'barometric_pressure', 'precipitation', 'incoming_solar_radiation', 'outgoing_solar_radiation', 'wind_speed', 'wind_direction', 'photosynthetically_active_radiation')
    for csv_value in csv_data:
        writer.writerow(csv_value)
    return response
