from django.shortcuts import render
from .models import Projects, AboutMe, Blog, WorkExperience, Education
from .forms import ContactForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f"Message from {form.cleaned_data['name']}"
            message = form.cleaned_data['message']
            sender_email = form.cleaned_data['email']
            full_message = f"From: {sender_email}\n\n{message}"

            send_mail(subject, full_message, sender_email, [settings.CONTACT_EMAIL])
            form = ContactForm()
            return render(request, 'portfolio/contact.html', {'form': form, 'success': True})

    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})



def home(request):
    blog = Blog.objects.all().order_by('-date')  # order by newest date first
    return render(request, 'portfolio/blog.html', {'blog': blog})


def about(request):
    about = AboutMe.objects.first()
    return render(request, 'portfolio/about.html', {'about': about})


def projects(request):
    projects = Projects.objects.prefetch_related('images').order_by('-start_date')
    return render(request, 'portfolio/projects.html', {'projects': projects})


def workExperience(request):
    work = WorkExperience.objects.all()
    return render(request, 'portfolio/workExperience.html', {'work': work})

def education(request):
    education = Education.objects.all()
    return render(request, 'portfolio/Education.html', {'education': education})