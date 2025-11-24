from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Project
from .forms import InquiryForm

def home(request):
    # Optional: Fetch 3 recent projects for the home page "Featured Work" section
    featured_projects = Project.objects.all().order_by('-created_at')[:3]
    return render(request, 'index.html', {'featured_projects': featured_projects})

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    # Fetch all projects from the database
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'portfolio.html', {'projects': projects})

def contact(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            # 1. Save the data to the database
            inquiry = form.save()
            
            # 2. Send Notification Email to YOU (Admin)
            subject_admin = f"New Inquiry: {inquiry.project_type} from {inquiry.first_name}"
            message_admin = f"""
            You have received a new inquiry!
            
            Name: {inquiry.first_name} {inquiry.last_name}
            Email: {inquiry.email}
            Project Type: {inquiry.project_type}
            
            Details:
            {inquiry.details}
            """
            
            send_mail(
                subject_admin,
                message_admin,
                settings.DEFAULT_FROM_EMAIL, # From
                [settings.DEFAULT_FROM_EMAIL], # To (Sends to yourself)
                fail_silently=False,
            )

            # 3. Send Confirmation Email to CUSTOMER
            subject_customer = "We received your inquiry - NAMKAATH"
            message_customer = f"""
            Hi {inquiry.first_name},

            Thank you for reaching out to NAMKAATH! 
            
            We have received your inquiry regarding "{inquiry.project_type}" and our team is reviewing the details. 
            We will get back to you shortly to discuss the next steps.

            Best regards,
            The NAMKAATH Team
            """
            
            send_mail(
                subject_customer,
                message_customer,
                settings.DEFAULT_FROM_EMAIL, # From
                [inquiry.email], # To (The customer's email)
                fail_silently=False,
            )

            # Return success page
            return render(request, 'get_started.html', {'form': InquiryForm(), 'success': True})
    else:
        form = InquiryForm()

    return render(request, 'get_started.html', {'form': form})