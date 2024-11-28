from django.shortcuts import render, redirect

from .forms import ContactForm

# import to email with mailtrap.io
from django.core.mail import EmailMessage

from django.urls import reverse

# Create your views here.

def contact(request):
    contact_form = ContactForm()
    
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            mail = request.POST.get('mail', '')
            content = request.POST.get('content', '')
            
            # create the content
            mail = EmailMessage(
                "la Sabrosa: Nuevo mensaje de contacto", #asunto
                "De {name} {mail} \n\nEscribió:\n\n {content}", #mensaje
                "lasabrosa.com", #email de origen
                ["mvictoria@mailtrap.io"], #email de destino
                reply_to=[mail],
            )
            
            # lo enviamos y redireccionamos
            try:
                mail.send()
                # todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                # algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")
    
    return render(request, 'contact.html', {'form':contact_form})