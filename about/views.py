from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ContactForm


def about_six(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    contact_form = ContactForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "contact_form": contact_form},
    )