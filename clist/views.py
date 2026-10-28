from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .form import ContactForm
from django.db.models import Q, F
from django.contrib.postgres.search import TrigramSimilarity


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'clist/contact_list.html', {'contacts': contacts})


def contact_detail(request, slug):
    contact = get_object_or_404(Contact, slug=slug)
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


def contact_search(request):
    search_text = request.GET.get('query')
    contacts = Contact.objects.none()
    if search_text:
        contacts = Contact.objects.annotate(name_similarity=TrigramSimilarity('first_name', search_text), last_name_similarity=TrigramSimilarity('last_name', search_text), phone_similarity=TrigramSimilarity('phone', search_text), address_similarity=TrigramSimilarity(
            'address', search_text)).filter(Q(name_similarity__gt=0.3) | Q(last_name_similarity__gt=0.3) | Q(phone_similarity__gt=0.3) | Q(address_similarity__gt=0.3)).order_by('-name_similarity', '-last_name_similarity', '-phone_similarity', '-address_similarity')

    # if not query:
    #     return render(request, 'contact_search.html', {'contacts': [], 'query': query})
    # # res_phone = Contact.objects.filter(phone__icontains=query)
    # # res_fname = Contact.objects.filter(first_name__icontains=query)
    # # res_lname = Contact.objects.filter(last_name__icontains=query)
    # # res_address = Contact.objects.filter(address__icontains=query)

    # # contacts = res_phone.union(res_fname, res_lname, res_address)
    # contacts = Contact.objects.filter(
    #     Q(phone__icontains=query) |
    #     Q(first_name__icontains=query) |
    #     Q(last_name__icontains=query) |
    #     Q(address__icontains=query)
    # )

    # context = {'contacts': contacts, 'query': query}
    # # print("CONTACT SEARCH VIEW EXECUTED")
    # return render(request, 'clist/contact_search.html', context)
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
