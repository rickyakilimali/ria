from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import BusinessProfile
from django.contrib.auth.models import User

# Create your views here.

class BusinessProfileDetailView(DetailView):

    model = User
    context_object_name = 'business' 
    template_name = 'businessprofile_detail.html'

    