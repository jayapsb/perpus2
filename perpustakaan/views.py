from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from perpustakaan.models import Buku, Customer, Transaksi
from perpustakaan.forms import FormBuku, FormKelompok, FormCustomer, FormTransaksi
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from perpustakaan.resource import BukuResource
import logging

# Create your views here... #

def index(request):
    context = {
        'Judul':'Web Application for E-Library',
        'Content':'Still Developing For this Application'
    }
    return render(request,'index.html',context)

def export_xls(request):
    buku = BukuResource()
    dataset = buku.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="laporan data buku.xlsx"'
    return response

@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Creating User Successfully")
            return redirect('signup')
        else:
            messages.error(request, "Failed Creating User, Please try again")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form':form,
        }
        return render(request, 'signup.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Successfully Changed")
            return redirect('ubah_buku', id_buku=id_buku) # diarahkan kembali ke halaman ubah data itu sendiri
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form':form,
            'buku':buku,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def ubah_customer(request, id_customer):
    customer = Customer.objects.get(id=id_customer)
    template = 'ubah-customer.html'
    if request.POST:
        form = FormCustomer(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Successfully Changed")
            return redirect('ubah_customer', id_customer=id_customer) # diarahkan kembali ke halaman ubah data itu sendiri
    else:
        form = FormCustomer(instance=customer)
        konteks = {
            'form':form,
            'customer':customer,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    buku.delete()
    messages.success(request, "Successfully Deleted")
    return redirect('buku') # kembali ke halaman url buku

@login_required(login_url=settings.LOGIN_URL)
def hapus_customer(request, id_customer):
    customer = Buku.objects.get(id=id_customer)
    customer.delete()
    messages.success(request, "Successfully Deleted")
    return redirect('customer') # kembali ke halaman url customer

@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    if request.POST:
        kata_kunci = request.POST['cari']
        books = Buku.objects.filter(judul__contains=kata_kunci)
        konteks = {
            'books': books,
        }
    else:
        books = Buku.objects.all()
        konteks = {
            'books': books,
        }
    return render(request, 'buku.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def transaksi(request):
    if request.POST:
        kata_kunci = request.POST['cari']
        transaksis = Transaksi.objects.filter(judul__contains=kata_kunci)
        konteks = {
            'transaksis': transaksis,
        }
    else:
        transaksis = Transaksi.objects.all()
        konteks = {
            'transaksis': transaksis,
        }
    return render(request, 'transaksi.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def lihat_transaksi(request, id_transaksi):
    transaksi = Transaksi.objects.get(id=id_transaksi)
    template = 'lihat_transaksi.html'
    
    if request.POST:
        form = FormTransaksi(request.POST, instance=transaksi)
    else:
        form = FormTransaksi(instance=transaksi)
        konteks = {
            'form':form,
            'transaksi':transaksi,
        }
    return render(request, template, konteks)


@login_required(login_url=settings.LOGIN_URL)
def customer(request):
    customers = Customer.objects.all()
    konteks = {
        'customers': customers,
    }
    return render(request, 'customer.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def penerbit(request):
    return render(request, 'penerbit.html')

@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Added")
            form = FormBuku()
            konteks = {
                'form': form,
            }
            return redirect('tambah_buku')
    else:
        form = FormBuku()
        konteks = {
            'form': form,
        }
    return render(request, 'tambah-buku.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def tambah_transaksi(request):
    if request.POST:
        form = FormTransaksi(request.POST)
        if form.is_valid():
            logging.warning(form)
            #print(form)
            form.save()
            messages.success(request, "Successfully Added")
            form = FormTransaksi()
            konteks = {
                'form': form,
            }
            return redirect('tambah_transaksi')
    else:
        form = FormTransaksi()
        konteks = {
            'form': form,
        }
    return render(request, 'tambah-transaksi.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def tambah_kelompok(request):
    form = FormKelompok()
    konteks = {
        'form': form,
    }
    return render(request, 'tambah-kelompok.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def tambah_customer(request):
    if request.POST:
        form = FormCustomer(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Added")
            form = FormCustomer()
            konteks = {
                'form': form,
            }
            return redirect('tambah_customer')
    else:
        form = FormCustomer()
        konteks = {
            'form': form,
        }
    return render(request, 'tambah-customer.html', konteks)