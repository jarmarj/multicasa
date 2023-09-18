# from django.contrib import messages
# from django.template.loader import get_template
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.shortcuts import render
from django.core.paginator import Paginator
from casas.models import Casa
from casas.forms import ClienteForm
import random

# Create your views here.

# generar pdf
def multicasa_pdf(request, id):
    casa = Casa.objects.get(id=id)
    # crear bytestream buffer
    buff = io.BytesIO()
    c = canvas.Canvas(buff, pagesize=letter, bottomup=0)
    # crear objeto de text
    textobject = c.beginText()
    textobject.setTextOrigin(inch, inch)
    textobject.setFont("Helvetica", 14)
    # lineas de texto del pdf
    lines = [
        '       BIENES RAICES MULTICASA',
        '       TU MEJOR OPCION EN AGENCIA DE BIENES RAICES',
        '',
        '',
        '',
        '-------------------------------------------------------------------------------------',
        '               Direccion:',
        '',
        f'                      Calle: {casa.calle}',
        f'                      Colonia: {casa.colonia}',
        f'                      Ciudad: {casa.ciudad}',
        f'                      Estado: {casa.estado}',
        f'                      Codigo Postal: {casa.cp}',
        '',
        '-------------------------------------------------------------------------------------',
        '',
        '               Detalles de la propiedad:',
        '',
        f'                      Precio: ${casa.precio} MXN',
        f'                      Baños: {casa.banos}',
        f'                      Recamaras: {casa.recamaras}',
        '-------------------------------------------------------------------------------------',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '           Este no es un comprobante de pago ni factura de ningun tipo.',
        '           Documento unicamente informativo.',
        '           Se prohibe su uso distinto a los establecidos en el programa.',
        '',
        '',
        '                                       Multicasa© S.A de C.V',
        '                                       Multicasa Inc.',
        '                                       Grupo Multicasa Asociados©',
        '                                       Grupo Multicasa Asociados Mexico ©',
    ]
    for line in lines:
        textobject.textLine(line)

    # Finis up
    c.drawText(textobject)
    c.showPage()
    c.save()
    buff.seek(0)

    # return something
    
    return FileResponse(buff, as_attachment=True, filename='multicasa.pdf')

def inicio(request):
    results_page = False
    items = list(Casa.objects.all())
    # change 3 to how many random items you want
    random_casas = random.sample(items, 5)
    # random_item = random.choice(items) # if you want only a single random item
    total_random_casas = len(random_casas)
    last_added = Casa.objects.filter(vendida=False).last()
    details_casa_page = False
    context = {
        'details_casa_page': details_casa_page,
        'total_casas': total_random_casas,
        'casas_encontradas': random_casas,
        'results_page': results_page,
        'last_added': last_added
    }
    return render(request, 'inicio.html', context=context)


def company(request):
    casas_encontradas = Casa.objects.all()
    lista_cantidad = list(Casa.objects.all())
    vendidas_cantidad = len(list(Casa.objects.filter(vendida=True)))
    no_vendidas_cantidad = len(list(Casa.objects.filter(vendida=False)))

    details_casa_page = False
    context = {
        'details_casa_page': details_casa_page,
        'vendidas_cantidad': vendidas_cantidad,
        'no_vendidas': no_vendidas_cantidad
    }
    return render(request, 'compania.html', context=context)


def company(request):
    details_casa_page = False,
    last_added = Casa.objects.filter(vendida=False).last()
    return render(request, 'compania.html', context={'details_casa_page': details_casa_page, 'last_added': last_added, 'details_casa_page': details_casa_page})


def servicios(request):
    details_casa_page = False
    last_added = Casa.objects.filter(vendida=False).last()
    return render(request, 'servicios.html', context={'details_casa_page': details_casa_page, 'last_added': last_added})


def requisitos(request):
    details_casa_page = False
    last_added = Casa.objects.filter(vendida=False).last()
    return render(request, 'requisitos.html', context={'details_casa_page': details_casa_page, 'last_added': last_added})


def contactos(request):
    details_casa_page = False
    last_added = Casa.objects.filter(vendida=False).last()
    return render(request, 'contactos.html', context={'details_casa_page': details_casa_page, 'last_added': last_added})


def dashboard(request):
    casas_saltillo = Casa.objects.filter(ciudad='Saltillo')
    casas_ramos = Casa.objects.filter(ciudad='Arteaga')
    casas_arteaga = Casa.objects.filter(ciudad='Ramos Arizpe')

    vendidas = Casa.objects.filter(vendida=True)
    no_vendidas = Casa.objects.filter(vendida=False)

    details_casa_page = False,
    last_added = Casa.objects.filter(vendida=False).last()
    context = {
        'vendidas':vendidas,
        'no_vendidas':no_vendidas,
        'casas_saltillo': casas_saltillo,
               'casas_ramos': casas_ramos,
               'casas_arteaga': casas_arteaga,
               'details_casa_page': details_casa_page,
               'last_added': last_added,
               'details_casa_page': details_casa_page}
    return render(request, 'dashboard.html', context=context)


def details(request, id):
    # id_casa = int(id)
    is_details = True
    casa = Casa.objects.get(id=id)
    last_added = Casa.objects.filter(vendida=False).last()
    detail_casa_page = True,
    context = {
        'detail_casa_page': detail_casa_page,
        'casa': casa, 'is_details': is_details, 'last_added': last_added
    }
    return render(request, 'detailsCasa.html', context=context)


def help(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ClienteForm()
    print(request.POST)
    details_casa_page = False
    last_added = Casa.objects.filter(vendida=False).last()
    return render(request, 'asesoria.html', context={'form': form, 'details_casa_page': details_casa_page, 'last_added': last_added})


def results(request):
    query = ''
    results_page = True
    err_message = "No tenemos casas con los filtros: "
    used_filters = list()
    filter_message = 'Filtro(s): '
    filters = [
        {0: 'ciudad', 's': 'Ciudad: '},
        {1: 'estado', 's': 'Estado: '},
        {2: 'cp', 's': 'CP: '},
        {3: 'precio-min', 's': 'Precio min: '},
        {4: 'precio-max', 's': 'Precio max: '},
        {5: 'recamaras', 's': 'Recamaras: '},
        {6: 'banos', 's': 'Baños: '}
    ]

    for index, filter in enumerate(filters):
        actual_filter = filter[index]
        r = request.GET[actual_filter]
        if r != '':
            err_message += filter['s'] + r + ' '
            used_filters.append(filter['s'] + r)

        if actual_filter.__eq__('ciudad'):
            ciudad = request.GET['ciudad']
        elif actual_filter.__eq__('estado'):
            estado = request.GET['estado']
        elif actual_filter.__eq__('cp'):
            cp = request.GET['cp']
        elif actual_filter.__eq__('precio-min'):
            min_precio = request.GET['precio-min']
            if min_precio == '':
                min_precio = '1'
            else:
                min_precio = float(request.GET['precio-min'])
        elif actual_filter.__eq__('precio-max'):
            max_precio = request.GET['precio-max']
            if max_precio == '':
                max_precio = '999999999'
            else:
                max_precio = float(request.GET['precio-max'])
        elif actual_filter.__eq__('recamaras'):
            recamaras = request.GET['recamaras']
            if recamaras == '':
                recamaras = '999'
            else:
                recamaras = int(request.GET['recamaras'])
        elif actual_filter.__eq__('banos'):
            banos = request.GET['banos']
            if banos == '':
                banos = '99'
            else:
                banos = int(request.GET['banos'])

    casas_encontradas = Casa.objects.filter(
        ciudad__icontains=ciudad,
        estado__icontains=estado,
        cp__icontains=cp,
        precio__range=(min_precio, max_precio),
        recamaras__lte=recamaras,
        banos__lte=banos
    )
    total_casas_encontradas = len(casas_encontradas)

    page = request.GET.get('page', 1)

    query += '?ciudad=' + request.GET.get('ciudad', '') + '&'
    query += 'estado=' + request.GET.get('estado', '') + '&'
    query += 'cp=' + request.GET.get('cp', '') + '&'
    query += 'precio-min=' + request.GET.get('precio-min', '') + '&'
    query += 'precio-max=' + request.GET.get('precio-max', '') + '&'
    query += 'recamaras=' + request.GET.get('recamaras', '') + '&'
    query += 'banos=' + request.GET.get('banos', '') + '&'
    query += 'page'

    try:
        page_size = 3
        # list objetos del request, cantidad por pag
        paginator = Paginator(casas_encontradas, page_size)
        casas_encontradas_pag = paginator.page(page)

    except:
        return render(request, 'results.html', context={'err_message': 'Algo salio mal con la busqueda!'})

    last_added = Casa.objects.filter(vendida=False).last()
    details_casa_page = False,
    context = {
        'details_casa_page': details_casa_page,
        'used_filters': used_filters,
        'filter_message': filter_message,
        'total_casas': total_casas_encontradas,
        'casas_encontradas': casas_encontradas_pag,
        'paginator': paginator,
        'max_precio': max_precio,
        'min_precio': min_precio,
        'err_message': err_message,
        'query': query,
        'results_page': results_page,
        'page_size': page_size,
        'last_added': last_added
    }
    return render(request, 'results.html', context=context)
