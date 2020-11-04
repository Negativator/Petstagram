from django.shortcuts import render, redirect

# Create your views here.
from pets.models import Pet, Like


def pet_all(req):
    all_pets = Pet.objects.all()
    context = {
        'all_pets': all_pets,
    }
    return render(req, 'pets/pet_list.html', context)


def pet_detail(req, pk):
    pet = Pet.objects.get(pk=pk)
    likes = len(Like.objects.filter(pet=pk))
    context = {
        'pet': pet,
        'likes': likes,
    }
    return render(req, 'pets/pet_detail.html', context)


def pet_like(req, pk):
    pet = Pet.objects.get(pk=pk)
    new_like = Like()
    new_like.pet = pet
    new_like.save()
    return redirect('pet_all')


def pet_delete(req):
    return render(req, 'pets/pet_delete.html')