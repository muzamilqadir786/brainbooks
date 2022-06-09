from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/sent.html')
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact/contact_us.html', context)
