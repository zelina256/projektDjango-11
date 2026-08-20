from django.shortcuts import render
from .models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

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