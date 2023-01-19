from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse

from accounts.models import Visiteur
from store.forms import addProductForm
from store.models import Product, Cart, Order, ShippingAddress


def index(request):
    products = Product.objects.all()
    query = request.GET.get('query')
    if not query:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(name__icontains=query)
        if not products.exists():
            products = Product.objects.filter(categorie__title__icontains=query)
        if not products.exists():
            message = "Misére de misére, nous avons trouvé aucun résultat!"
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'store/index.html', context={"products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', context={"product": product})

def add_to_cart(request, slug):
   user = request.user
   product = get_object_or_404(Product, slug=slug)
   cart, _ = Cart.objects.get_or_create(user=user)
   order, created = Order.objects.get_or_create(user=user,ordered=False, product=product)
   if created:
      cart.orders.add(order)
      cart.save()
   else:
      order.quantity += 1
      order.save()
   return redirect(reverse("index"))
   #return redirect(reverse("product",kwargs={"slug": slug}))

def cart(request):
    cart = get_object_or_404(Cart, user = request.user)
    total=cart.get_cart_total()
    ordertotal=cart.get_ordertotal()
    return render(request, 'store/cart.html', context={"orders": cart.orders.all(), "total":total, "ordertotal": ordertotal})

def delete_cart(request):
    #cart = request.user.cart
    if cart := request.user.cart:
        #cart.orders.all().delete()
        cart.delete()
    return redirect('checkout')
def add_product(request):
    if request.method == "POST":
        form = addProductForm(request.POST)
        form.save()
    else:
        form = addProductForm()
    return render(request, 'store/add_product.html', context={"form": form})

def checkout(request):
    if request.method == "POST":
        items = request.POST.get("items")
        user = request.user
        address = request.POST.get("address")
        email = request.POST.get("email")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zipcode = request.POST.get("zipcode")
        visiteur = ShippingAddress(items=items, address=address,email=email, city=city, user=user, state=state, zipcode=zipcode)
        visiteur.save()
    cart = get_object_or_404(Cart, user=request.user)
    total = cart.get_cart_total()
    ordertotal = cart.get_ordertotal()
    return render(request, 'store/checkout.html',context={"orders": cart.orders.all(), "total": total, "ordertotal": ordertotal})

