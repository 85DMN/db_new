from django.shortcuts import render
from django.http import HttpResponse
from phones.models import Phone

def show_catalog(request):
    template = 'catalog.html'
    caro = Phone.objects.all()
    print(caro.order_by('price'),'#######')
    caro = caro.order_by('price')
    context = {caro}
    return render(
        request,
        template,
        context
    )

def list_phone(request):
    template = 'base.html'
    caro = Phone.objects.all()
    print(caro.order_by('price'),'#######')
    caro = caro.order_by('price')
    # cars = [f'{c.name}, стоимость: {c.price}, {c.image}' for c in caro]
    # context = {caro}
    return render(
                request,
                template,
                caro
    )#HttpResponse('<br>'.join(cars))

    
# def create_csv(request):
#     fg = csv.reader('phones.csv',delimiter=';')
#     print('______')
#     for row in fg:
#         print(row)

#     return HttpResponse('Все ok!!!')
