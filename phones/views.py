from django.shortcuts import render
from django.http import HttpResponse
from phones.models import Phone

def show_catalog(request):

    # if sd != None:
    template = 'catalog.html'

    # caro = Phone.objects.all()
    caro = Phone.objects.all()
    if 'nm' in request.GET:
        caro = caro.order_by('name')
    elif 'prd' in request.GET: 
        caro = caro.order_by('-price')
    elif 'prh' in request.GET: 
        caro = caro.order_by('price')
    else: 
        caro = caro
    # else:
    #     template = 'catalog_d.html'
    #     print(sd,'+++++++++++++')
    #     caro = Phone.objects.filter(slug__icontains = sd)
    # print(caro.order_by('price'),'#######')
    
    return render(
        request,
        template,
        {'caro':caro}
    )

def show_catalogd(request,sd):
    template = 'catalog_d.html'
    print(sd,'+++++++++++++')
    caro = Phone.objects.filter(slug__icontains = sd)
    # print(caro.order_by('price'),'#######')
    
    return render(request,template,{'caro':caro})#HttpResponse('<br>'.join(cars))

# def create_csv(request):
#     fg = csv.reader('phones.csv',delimiter=';')
#     print('______')
#     for row in fg:
#         print(row)

#     return HttpResponse('Все ok!!!')
