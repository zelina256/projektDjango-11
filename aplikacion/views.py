from django.shortcuts import render
from .models import *
from django.contrib import messages
# Create your views here.
def home(request):
    # Variable = Modeli.objects.metoda
    # .all() - merr te gjitha te dhenat nga modeli => for in tek html
    categories = Category.objects.all()
    context = {"categories":categories}
    return render(request, "home.html", context)

def about(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "about.html", context)


def category(request, slug):
    categories = Category.objects.all()
    # Marrim vetem te dhenen per nje categori/informacion
    # Variable = Modeli.objects.metoda
    # .get() - merr vetem nje te dhene nga modeli
    # brenda () duhet te vendoset "kusht"
    detail_cat = Category.objects.get(category_slug=slug)
    # Marrim te gjitha elementet qe i perkasin nje kategorie
    # Variable = Modeli.objects.metoda
    # .filter() - merr te gjitha te dhenat nga modeli duke vendosur nje kusht
    # .filter => for in
    category_items = Item.objects.filter( item_category =detail_cat)
    context = {"categories": categories, "detail_cat": detail_cat, "category_items": category_items}
    return render(request, "category.html", context)







def contact(request):
    # ti tregojme qe metoda eshte post (do marre informacion nga fusha e inputeve)
    if request.method == "POST":
        # Krijimi i variblave qe informacionet nga input te ruhen ne view
        # emerCfaredo = request.POST['vlera e atributit name tek input']
        firstName =request.POST['firstName']
        lastName =request.POST['lastName']
        email =request.POST['email']
        comment =request.POST['comment']
        # Kushtin nese input nuk jane boshe informacionet do te ruhen
        if firstName != "" and lastName !="" and email !="" and comment !="":
        # Informacionet qe jane ne view te kalonet tek class/model dhe te ruhen
            Contact(
                # Emri i fushes se class = emrin e variablit tek request.POST
                contact_firstName = firstName,
                contact_lastName = lastName,
                contact_email = email,
                contact_comment = comment   
            ).save()
            # Afishimi i mesazhit
            messages.success(request, "Thank you, Message send!")
        # Nese fushat nuk jane te plotesuara
        else:
            messages.error(request, "Message not send!")
        # .save() ruan informacionet
    return render(request, "contact.html")