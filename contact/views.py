# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ContactForm


@login_required
def contact_view(request):

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'We have recieved your qoute request '
                             'and we will get back to you soon!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add contact form.'
                           'Please ensure the form is valid.')
    else:
        form = ContactForm()

    template = 'contact/contact_view.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
