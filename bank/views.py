from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from .models import Client, Account, Credit


class ClientView(generic.ListView):
    model = Client
    template_name = 'clients.html'
    context_object_name = 'clients_list'


class ClientDetailView(generic.DetailView):
    model = Client
    template_name = 'detail_client.html'
    context_object_name = 'client'

