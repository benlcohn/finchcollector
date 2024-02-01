import os
import uuid

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Food
from .forms import FeedingForm

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {
    'finches': finches
  })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)

  id_list = finch.foods.all().values_list('id')
  foods_finch_doesnt_eat = Food.objects.exclude(id__in=id_list)

  feeding_form = FeedingForm()
  return render(request, 'finches/detail.html', { 
    'finch': finch, 'feeding_form': feeding_form,
    'foods': foods_finch_doesnt_eat
    })

def add_feeding(request, finch_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
  model = Finch
  fields = ['name', 'breed', 'description', 'age']

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['name', 'breed', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'


class FoodList(ListView):
  model = Food

class FoodDetail(DetailView):
  model = Food

class FoodCreate(CreateView):
  model = Food
  fields = '__all__'

class FoodUpdate(UpdateView):
  model = Food
  fields = ['name', 'prep']

class FoodDelete(DeleteView):
  model = Food
  success_url = '/foods'

def assoc_food(request, finch_id, food_id):
  Finch.ojects.get(id=finch_id).foods.add(food_id)
  return redirect('detail', finch_id=finch_id)

def unassoc_food(request, finch_id, food_id):
  Finch.ojects.get(id=finch_id).foods.remove(food_id)
  return redirect('detail', finch_id=finch_id)