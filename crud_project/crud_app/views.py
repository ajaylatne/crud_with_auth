from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Items
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login_url')
def order_view(request):
    template_name = 'crud_app/order_form.html'
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_order_url')
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='login_url')
def show_order(request):
    template_name = 'crud_app/all_orders.html'
    data = Items.objects.all()
    context = {'data': data}
    return render(request, template_name, context)


def update_view(request, pk):
    template_name = 'crud_app/order_form.html'
    obj = Items.objects.get(pk=pk)
    form = ItemForm(instance=obj)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('all_order_url')
    context = {'form': form}
    return render(request, template_name, context)


def delete_view(request, pk):
    obj = Items.objects.get(pk=pk)
    template_name = 'crud_app/confirmation.html'
    if request.method == 'POST':
        obj.delete()
        return redirect('all_order_url')
    return render(request, template_name)
