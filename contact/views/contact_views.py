from django.shortcuts import render, get_list_or_404
from contact.models import Contact

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - ',
    }
    return render(request, 'contact/index.html',context)

def contact(request, contact_id):
    # Contact.objects.get(pk=contact_id)
    single_contact = get_list_or_404(
        Contact.objects.filter(id=contact_id, show=True)
    )
    site_title = f'{single_contact.first_name} {single_contact.last_name} - '
    context = {
        'contacts': single_contact,
        'site_title': site_title,
    }
    return render(request, 'contact/contact.html',context)

def search(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - ',
    }
    return render(request, 'contact/index.html',context)