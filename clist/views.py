from django.shortcuts import render, redirect
from .models import Contact
from .form import ContactForm


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'clist/contact_list.html', {'contacts': contacts})


def contact_detail(request, slug):
    contact = Contact.objects.get(slug=slug)
    context = {'contact': contact}
    return render(request, 'clist/contact_detail.html', context)


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clist:contact_list')
    else:
        form = ContactForm()

    return render(request, 'forms/add_contact.html', {'form': form})
# def add_contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('add_contact:add_contact')
#         else:
#             form = ContactForm()
#         return render(request, 'forms/add_contact.html', {'form': form})

# from django.shortcuts import render, redirect
# from .models import Contact
# from .form import ContactForm


# def contact_list(request):
#     contacts = Contact.objects.all()
#     return render(request, 'clist/contact_list.html', {'contacts': contacts})


# def contact_detail(request, slug):
#     contact = Contact.objects.get(slug=slug)
#     context = {'contact': contact}
#     return render(request, 'clist/contact_detail.html', context)
