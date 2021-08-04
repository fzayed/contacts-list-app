from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Contacts

class ContactList(ListView):
    model = Contacts
    context_object_name = 'contacts'
    template_name = 'project/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['contacts'] = context['contacts'].filter(name__icontains=search_input)
        
        context['search_input'] = search_input
        return context

class ContactDetail(DetailView):
    model = Contacts
    context_object_name = 'contact'
    template_name = 'project/contact_info.html'

class ContactCreate(CreateView):
    model = Contacts
    fields = '__all__'
    success_url = reverse_lazy('contacts')
    template_name = 'project/create.html'

class ContactUpdate(UpdateView):
    model = Contacts
    fields = '__all__'
    success_url = reverse_lazy('contacts')
    template_name = 'project/update.html'

class ContactDelete(DeleteView):
    model = Contacts
    context_object_name = 'contact'
    success_url = reverse_lazy('contacts')
    template_name = 'project/delete.html'
