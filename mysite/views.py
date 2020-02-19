from django.shortcuts import render
import requests,json
from .models import Contact

# Create your views here.
def index(request):
    return render(request, "mysite/index.html")

def result(request):
    return render(request, "mysite/result.html")


def testFile(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        c = Contact(email=email, phone=phone, address=address)
        c.save()

        return render(request, "mysite/result.html")
    else:
        return render(request, "mysite/testFile.html")

def autogen(request):
    return render(request, "mysite/autogen.html")

def chuck(request):
    if request.method == 'POST':
        return render(request, "mysite/result.html")
    return render(request, "mysite/chucknoris.html")
