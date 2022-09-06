# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TestimonialForm


@login_required
def add_testimonial(request):
    """ Add a testimonial to the store """

    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save()
            messages.success(request, 'Successfully added testimonial!')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Failed to add testimonial.'
                           'Please ensure the form is valid.')
    else:
        form = TestimonialForm()

    template = 'testimonials/testimonials.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
