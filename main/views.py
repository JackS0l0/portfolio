from django.shortcuts import render
from .models import WelcomeText,Aboutme,Projects,Phone,Whatsapp,Telegram,Location
def index(request):
    data={
        'title': "Javidan Babayev's portfolio",
        'welcometext': WelcomeText.objects.all()[0:1],
        'aboutmeleft': Aboutme.objects.all()[0:3],
        'aboutmeright': Aboutme.objects.all()[3:6],
        'projectsup': Projects.objects.all().order_by('-date')[0:5],
        'projectsdown': Projects.objects.all().order_by('-date')[5:10],
        'phone': Phone.objects.all()[0:1],
        'whatsapp': Whatsapp.objects.all()[0:1],
        'telegram': Telegram.objects.all()[0:1],
        'location': Location.objects.all()[0:1],
    }
    return render(request,'index.html',data)