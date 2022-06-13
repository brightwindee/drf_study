from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from .models import Photo
from .forms import PhotoForm

# Create your views here.
def index(request: HttpRequest):
    return HttpResponse("<b>Hello Photo Web</b>")


def photo_index(request: HttpRequest):
    photos = Photo.objects.all()
    return render(request, 'photo/photo_list.html', {'photos': photos})


def photo_detail(request: HttpRequest, id):
    print("[photo_detail]: ")
    photo = get_object_or_404(Photo, pk=id)
    return render(request, 'photo/photo_detail.html', {'photo': photo})


def photo_post(request: HttpRequest):
    if request.method == "POST":
        print("[photo_post]: post")
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('photo_detail', id=photo.pk)
    else:
        print("[photo_post]: get")
        form = PhotoForm()

    return render(request, 'photo/photo_post.html', {'form': form})

def photo_edit(request: HttpRequest, id):
    photo = get_object_or_404(Photo, pk=id)
    if request.method == "POST":
        print("[photo_edit]: %d, post" % id)
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('photo_detail', id=photo.pk)
    else:
        print("[photo_edit]: %d, get" % id)
        form = PhotoForm(instance=photo)

    return render(request, 'photo/photo_post.html', {'form': form})
