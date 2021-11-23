from django.shortcuts import render
from .models import Products,Category
from django.db.models import Count
from django.core.paginator import Paginator , EmptyPage , InvalidPage

# Create your views here.
def index(request):
    allcategory = Category.objects.all()
    topviewproducts = Products.objects.all().order_by('product_view')[:20]
    bar1products = Products.objects.all().filter(product_category="ตู้เย็น").order_by('product_view')[:20]
    bar2products = Products.objects.all().filter(product_category="ทีวี").order_by('product_view')[:20]
    bar3products = Products.objects.all().filter(product_category="ที่นอน").order_by('product_view')[:20]
    bar4products = Products.objects.all().filter(product_category="เครื่องนอน").order_by('product_view')[:20]
    return render(request, 'frontend/main.html', {"allcategory":allcategory,"topviewproducts":topviewproducts,"bar1products":bar1products,"bar2products":bar2products,"bar3products":bar3products,"bar4products":bar4products})


# Create your views here.
def categorys(request,cat_name):
    # categoryname = Products.objects.get(product_category=cat_name)
    allcategory = Category.objects.all()
    products = Products.objects.all().filter(product_category=cat_name)
    topviewproducts = Products.objects.all().filter(product_category=cat_name).order_by('product_view')[:20]
    productscount = len(products)
    productall = Products.objects.all().filter(product_category=cat_name)
    
    paginator = Paginator(productall,50)
    try:
        page = int(request.GET.get('page','1'))
    except :
        page = 1

    try:
        Productsperpage = paginator.page(page)
    except (EmptyPage,InvalidPage):
        Productsperpage = paginator.page(paginator.num_pages)

    return render(request, 'frontend/category.html', {"allcategory":allcategory,'products':products,'topviewproducts':topviewproducts,'cat_name':cat_name,"productscount":productscount,'productall':Productsperpage})

def productdetails(request,product_name):
    allcategory = Category.objects.all()
    singleProducts = Products.objects.get(product_title=product_name)
    singleProducts.product_view = singleProducts.product_view+1

    lazadaprice = singleProducts.product_price +200
    shopeeprice = singleProducts.product_price +20
    # singleProducts.save()

    return render(request, 'frontend/productdetail.html',{"allcategory":allcategory,'product_name':product_name,'singleProducts':singleProducts,"lazadaprice":lazadaprice,"shopeeprice":shopeeprice})

def policy(request):
    return render(request, 'frontend/policy.html')