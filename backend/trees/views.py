from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tree, Region
from datetime import datetime
from django.views.generic import ListView
from django import forms
# Create your views here.


class TreeList(ListView):
    template_name = 'trees/trees.html'
    model = Tree

class RegionList(ListView):
    template_name = 'trees/regions.html'
    model = Region


class TreeForm(forms.ModelForm):
    class Meta:
        model = Tree
        fields = ['kind', 'region', 'last_harvest', 'last_chop', 'last_wasp', 'notes']
        widgets = {
            'last_wasp': forms.DateTimeInput(),
            'last_harvest': forms.DateTimeInput(),
            'last_chop': forms.DateTimeInput()
        }


class TreeCreate(CreateView):
    form_class = TreeForm
    model = Tree
    success_url="/tree/"


class RegionCreate(CreateView):
    model = Region
    fields = ["name", 'map_area', 'nw_marker', 'sw_marker', 'ne_marker', 'se_marker']
    success_url="/region/"


class TreeUpdate(UpdateView):
    model = Tree
    fields = ['kind', 'region', 'notes', 'last_chop', 'last_harvest', 'last_wasp']
    success_url="/tree/"


class RegionUpdate(UpdateView):
    model = Region
    fields = ["name", 'map_area', 'nw_marker', 'sw_marker', 'ne_marker', 'se_marker']
    success_url="/region/"



def report_wasp(request, tree_id):
    tree = Tree.get(pk=tree_id)
    tree.last_wasp = datetime.now()
    tree.save()
    

def report_harvest(request):
    tree = Tree.get(pk=tree_id)
    tree.last_harvest = datetime.now()
    tree.save()
