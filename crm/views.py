from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model
from .forms import ContactForm
from django.contrib import messages
from .models import *
from django.db.models import Q
import re
from django.core.exceptions import ValidationError

User = get_user_model()


def business_onboarding(request):
    email = request.user.email
    username = email.split('@')[0]
    return render(request, 'businesses/onboarding.html', {'username':username})







def contacts_list(request):
    contacts = Contact.objects.all()
    context = {}
    
    
    if request.GET:
        query = request.GET.get('q')
        queryset_name = Contact.objects.filter(
            Q(first_name__icontains=query)| 
            Q(middle_name__icontains=query)| 
            Q(last_name__icontains=query)
        )
        queryset_email = Contact.objects.filter(
            Q(email__icontains=query)
        )
        queryset_company = Contact.objects.filter(
            Q(company__icontains=query)
        )
        print('names: ', queryset_name)
        print('emails: ', queryset_email)
        print('companies: ', queryset_company)
        context = {
        'queyset_name':queryset_name,
        'queryset_email':queryset_email,
        'queryset_company':queryset_company
    }

    context = {
        'contacts': contacts
    }
    
#    9bGj!yp7bYf4TtE SUPABASE PASSWORD 
    return render(request, 'crm/contacts/contacts_list.html', context)

def create_contact(request):
    tags = Tag.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact created successfully!')
            return redirect('contacts_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return render(request, 'crm/contacts/new_contact.html', {'form': form, 'tags': tags})

    form = ContactForm()
    return render(request, 'crm/contacts/new_contact.html', {'form': form, 'tags':tags})

def edit_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, f'Contact {contact.first_name} {contact.last_name} updated!')
            return redirect('contacts_list')
        else:
            messages.error(request, 'Correct the form fields!')
            return render(request, 'crm/contacts/new_contact.html', {'form': form})
    else:
        form = ContactForm(instance=contact)
    return render(request, 'crm/contacts/new_contact.html', {'form': form, 'contact': contact})


def delete_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    messages.success(request, 'Contact deleted!')
    return redirect('contacts_list')
   
    
def tags_list(request):
    tags = Tag.objects.all()
    for tag in tags:
        tag_data = []
        

    return render(request, 'crm/contacts/tags_list.html', {'tags':tags})


def create_tag(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        tag = Tag.objects.create(name=name, created_by=request.user)
        tag.save()
        messages.success(request, f'Tag {tag.name} created successfully!')
        return redirect('tags_list')
    return render(request, 'crm/contacts/create_tag.html')

def edit_tag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    if request.method == 'POST':
        if tag:
            tag.name = request.POST.get('name')
            tag.save()
            messages.success(request, f'Tag {tag.name} updated successfully!')
            return redirect('tags_list')
        else:
            messages.success(request, f'Error retrieving tag')
            return redirect('tags_list')
    else:
        return render(request, 'crm/contacts/edit_tag.html')
    

def delete_tag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    if tag:
        tag.delete()
        messages.success(request, 'Tag deleted successfully!')
        return redirect('tags_list')
    
