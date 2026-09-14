from django.shortcuts import render
from .models import Contact


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'clist/contact_list.html', {'contacts': contacts})


def contact_detail(request, slug):
    contact = Contact.objects.get(slug=slug)
    context = {'contact': contact}
    return render(request, 'clist/contact_detail.html', context)
