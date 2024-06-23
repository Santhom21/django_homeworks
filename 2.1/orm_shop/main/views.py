from django.shortcuts import render, get_object_or_404
from main.models import Car, Sale
from django.http import Http404

def cars_list_view(request):
    cars = Car.objects.all()
    template_name = 'main/list.html'
    context = {'cars': cars}
    return render(request, template_name, context)

def car_details_view(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    template_name = 'main/details.html'
    context = {'car': car}
    return render(request, template_name, context)

def sales_by_car(request, car_id):
    try:
        car = Car.objects.get(pk=car_id)
        sales = Sale.objects.filter(car=car)
        template_name = 'main/sales.html'
        context = {'car': car, 'sales': sales}
        return render(request, template_name, context)
    except Car.DoesNotExist:
        raise Http404('Car not found')
