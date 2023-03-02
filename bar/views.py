from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .models import ItemCard, Extras
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .forms import LoginForm
from io import BytesIO, StringIO
from PIL import Image, ImageOps
from django.core.files.base import ContentFile


class LoginView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)

        context = {'form': form}

        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)

            return HttpResponseRedirect('/')

        return render(request, 'login.html', {'form': form})


@login_required
def user_logout(request):
    request.user.set_unusable_password()
    logout(request)

    return HttpResponseRedirect("/checklists")
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def menu(request):

    items = ItemCard.objects.all()

    context = {"items": items}

    return render(request, "menu.html", context)


@login_required
def add_item(request):

    return render(request, "add_item.html")


@login_required
def save_item(request):
    request_dict = request.POST.dict()

    item_photo = handle_photo(request)

    new_item = ItemCard.objects.create(name=request_dict['name'], ingredients=request_dict['ingredients'],
                                       volume=request_dict['volume'], photo=item_photo)

    extras_ids = []
    for key, value in request_dict.items():
        if "input" in key:
            extra_list_number = key.split("_")[1]
            extra_name = value

            new_extra = Extras.objects.create(list_number=extra_list_number, name=extra_name)
            new_extra.save()
            extras_ids.append(new_extra.id)

    new_item.extras.set(Extras.objects.filter(id__in=extras_ids))

    new_item.save()

    return HttpResponseRedirect("/Меню")


def handle_photo(request):
    for key, value in request.FILES.items():

        img_io = BytesIO()
        optimized_image = Image.open(value)
        optimized_image = ImageOps.exif_transpose(optimized_image)
        optimized_image.save(img_io, format='PNG', quality=60, optimized=True)
        img_content = ContentFile(img_io.getvalue(), str(value))

        return img_content


@login_required
def update_item(request, item_id):

    request_dict = request.POST.dict()

    print(request_dict)

    item_object = ItemCard.objects.get(id=item_id)

    for key, value in request.FILES.items():
        if str(value).endswith(('.png', 'jpg', 'gif', 'svg', 'jpeg')):
            print("new photo")
            new_photo = handle_photo(request)
            item_object.photo = new_photo

    if request_dict['name']:
        item_object.name = request_dict['name']

    if request_dict['ingredients']:
        item_object.name = request_dict['ingredients']

    if request_dict['volume']:
        item_object.name = request_dict['volume']

    extras_ids = []
    for key, value in request_dict.items():
        if "input" in key:
            extra_list_number = key.split("_")[1]
            extra_name = value

            new_extra = Extras.objects.create(list_number=extra_list_number, name=extra_name)
            new_extra.save()
            extras_ids.append(new_extra.id)

    item_object.extras.set(Extras.objects.filter(id__in=extras_ids))

    item_object.save()

    return HttpResponseRedirect('/Меню')


@login_required()
def edit_item(request, item_id):

    item = ItemCard.objects.get(id=item_id)

    extras = item.extras.order_by("list_number")

    return render(request, "edit_item.html", {"item": item, "extras": extras})


@login_required()
def change_status(request, item_id, status):
    item_object = ItemCard.objects.get(id=item_id)
    if status == "True":
        item_object.available = True
    else:
        item_object.available = False
    item_object.save()

    return HttpResponseRedirect('/Меню')
