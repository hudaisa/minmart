from django.shortcuts import redirect, render
from mart.forms import UploadForm
from .models import *
from django.core.mail import send_mail
# Create your views here.

def index (request):
    if request.GET:
        form = UploadForm(request.GET, request.FILES)
        if form.is_valid():
            form.save()
    reviews = Review.objects.all()
    context = {'reviews': reviews, 'form' : UploadForm}
    return render (request , 'index.html', context) 

def about(request):
    return render(request , 'about.html')

def review(request):
    if request.GET:
        form = UploadForm(request.GET, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(review)    
    return render(request , 'review.html' ,  {'form' : UploadForm})

def contact(request):
    if request.method == 'POST':
        mail = request.POST.get('email' , False);
        send_mail(
                'Welcome to minmart',
                'Thankyou for contacting us ....Our customer service team will respond you as soon as possible.',
                'min332759@gmail.com',
                [mail],
                fail_silently = False        
        )    
        return redirect(index)
    return render(request , 'contact.html')

def chocolates(request):
    chocolates = Chocolate.objects.all()
    context = {'chocolates': chocolates}

    return render(request , 'chocolates.html', context)

def beverages(request):
    beverages = Beverages.objects.all()
    context = {'beverages': beverages}

    return render(request , 'beverages.html', context)

def edible_items(request):
    edible_items = Edibleitems.objects.all()
    context = {'edible_items': edible_items}

    return render(request , 'edible.html', context)

def dairyproduct(request):
    dairyproduct = Dairyproduct.objects.all()
    context = {'dairyproduct': dairyproduct}
    return render(request , 'dairyproduct.html', context)    

def oil_ghee(request):
    oil_ghee = Oil_ghee.objects.all()
    context = {'oil_ghee': oil_ghee}
    return render(request , 'oil_ghee.html', context)    

def personal_care(request):
    personal_care = Personal_care.objects.all()
    context = {'personal_care': personal_care}
    return render(request , 'personal_care.html', context)    

def spices(request):
    spices = Spices.objects.all()
    context = {'spices': spices}
    return render(request , 'spices.html', context)
    
def staples(request):
    staples = Staples.objects.all()
    context = {'staples': staples}
    return render(request , 'staples.html', context)    

def tea_coffee(request):
    tea_coffee = Tea_coffee.objects.all()
    context = {'tea_coffee': tea_coffee}
    return render(request , 'tea_coffee.html', context)    

def fruits_vegetable(request):
    fruits_vegetable = Fruits_vegetable.objects.all()
    context = {'fruits_vegetable': fruits_vegetable}
    return render(request , 'fruits_vegetable.html', context)    

def bakery_items(request):
    bakery_items = Bakery_items.objects.all()
    context = {'bakery_items': bakery_items}
    return render(request , 'bakery_items.html', context)
    
def ready_to_eat(request):
    ready_to_eat = Ready_to_eat.objects.all()
    context = {'ready_to_eat': ready_to_eat}
    return render(request , 'ready_to_eat.html', context)    

def icecream_desert(request):
    icecream_desert = Icecream_desert.objects.all()
    context = {'icecream_desert': icecream_desert}
    return render(request , 'icecream_desert.html', context)    

def snacks(request):
    snacks = Snacks.objects.all()
    context = {'snacks': snacks}
    return render(request , 'snacks.html', context)

def fruit_nut(request):
    fruit_nut = Fruit_nut.objects.all()
    context = {'fruit_nut': fruit_nut}
    return render(request , 'fruit_nut.html', context)   

def search(request):
    query = request.GET['query']
    snacks = Snacks.objects.filter(snacks_name__icontains=query)
    icecream_desert = Icecream_desert.objects.filter(icecream_desert_name__icontains=query)
    bakery_items = Bakery_items.objects.filter(bakery_items_name__icontains=query)
    chocolates = Chocolate.objects.filter(chocolate_name__icontains=query)
    dairyproduct = Dairyproduct.objects.filter(dairyproduct_name__icontains=query)
    oil_ghee = Oil_ghee.objects.filter(oil_ghee_name__icontains=query)
    personal_care = Personal_care.objects.filter(personal_care_name__icontains=query)
    spices = Spices.objects.filter(spices_name__icontains=query)
    staples = Staples.objects.filter(staples_name__icontains=query)
    tea_coffee = Tea_coffee.objects.filter(tea_coffee_name__icontains=query)
    fruits_vegetable = Fruits_vegetable.objects.filter(fruits_vegetable_name__icontains=query)
    ready_to_eat = Ready_to_eat.objects.filter(ready_to_eat_name__icontains=query)
    fruit_nut = Fruit_nut.objects.filter(fruit_nut_name__icontains=query)
    beverages = Beverages.objects.filter(beverages_name__icontains=query)
    edible_items = Edibleitems.objects.filter(edibleitems_name__icontains=query)

    if query == '':
        return render(request , 'search.html', )
    else:
        params = {'snacks': snacks ,'icecream_desert': icecream_desert, 'bakery_items': bakery_items, 'chocolates': chocolates, 'dairyproduct': dairyproduct, 'oil_ghee': oil_ghee, 'personal_care': personal_care, 'spices': spices, 'staples': staples, 'tea_coffee': tea_coffee, 'fruits_vegetable': fruits_vegetable, 'ready_to_eat': ready_to_eat, 'fruit_nut': fruit_nut, 'edible_items': edible_items, 'beverages': beverages}
        return render(request, 'search.html' , params)
def checkout(request):
        if request.method == 'POST':
            email = request.POST.get('form-control', False);
            name = request.POST.get('name', False);
            message = 'Dear '+ name + ', Your order has been successfully placed and will be delivered at the given address within 20 - 30 minutes. For further queries, mail us at min332759@gmail.com Thanks for Shopping!'
            send_mail(
                    'Welcome to Minmart',
                    message,
                    'min332759@gmail.com',
                    [email],
                    fail_silently = False        
            )
            return redirect(index)
        return render(request, 'checkout (1).html')
    
def product_detail(request, id):
    beverages = Beverages.objects.filter(id = id).first()
    dict = {
        'beverages': beverages
    }
    return render(request, 'product_detail.html', dict)

def product_detail2(request, id):
    dairyproduct = Dairyproduct.objects.filter(id = id).first()
    dict = {
        'dairyproduct': dairyproduct
    }
    return render(request, 'product_detail2.html', dict)

def product_detail3(request, id):
    chocolate = Chocolate.objects.filter(id = id).first()
    dict = {
        'chocolate': chocolate
    }
    return render(request, 'product_detail3.html', dict)

def product_detail4(request, id):
    edible_items = Edibleitems.objects.filter(id = id).first()
    dict = {
        'edible_items': edible_items,
    }
    return render(request, 'product_detail4.html', dict)

def product_detail5(request, id):
    bakery_items = Bakery_items.objects.filter(id = id).first()
    dict = {
        'bakery_items': bakery_items,
    }
    return render(request, 'product_detail5.html', dict)

def product_detail6(request, id):
    fruits_vegetable = Fruits_vegetable.objects.filter(id = id).first()
    dict = {
        'fruits_vegetable': fruits_vegetable,
    }
    return render(request, 'product_detail6.html', dict)

def product_detail7(request, id):
    icecream_desert = Icecream_desert.objects.filter(id = id).first()
    dict = {
        'icecream_desert': icecream_desert,
    }
    return render(request, 'product_detail7.html', dict)

def product_detail8(request, id):
    oil_ghee = Oil_ghee.objects.filter(id = id).first()
    dict = {
        'oil_ghee': oil_ghee,
    }
    return render(request, 'product_detail8.html', dict)

def product_detail9(request, id):
    personal_care = Personal_care.objects.filter(id = id).first()
    dict = {
        'personal_care': personal_care,
    }
    return render(request, 'product_detail9.html', dict)

def product_detail10(request, id):
    ready_to_eat = Ready_to_eat.objects.filter(id = id).first()
    dict = {
        'ready_to_eat': ready_to_eat ,
    }
    return render(request, 'product_detail10.html', dict)

def product_detail11(request, id):
    tea_coffee = Tea_coffee.objects.filter(id = id).first()
    dict = {
        'tea_coffee': tea_coffee ,
    }
    return render(request, 'product_detail11.html', dict)

def product_detail12(request, id):
    snacks = Snacks.objects.filter(id = id).first()
    dict = {
        'snacks': snacks ,
    }
    return render(request, 'product_detail12.html', dict)

def product_detail13(request, id):
    spices = Spices.objects.filter(id = id).first()
    dict = {
        'spices': spices ,
    }
    return render(request, 'product_detail13.html', dict)

def product_detail14(request, id):
    staples = Staples.objects.filter(id = id).first()
    dict = {
        'staples': staples ,
    }
    return render(request, 'product_detail14.html', dict)