from django.shortcuts import render
from .forms import PhoneForm

# Create your views here.


def index_view(request):
    form = PhoneForm()
    context = {
        'form':form,
    }
    return render(request, "pages/index.html", context)

def contact_view(request):
    return render(request, "pages/contact.html", {})


def about_view(request):
    return render(request, "pages/about.html", {})


def privacy_view(request):
    return render(request, "pages/privacy.html", {})
