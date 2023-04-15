from gc import enable
from django.forms import ModelForm, CharField
from django import forms
from perpustakaan.models import Buku, Kelompok, Customer, Transaksi
from django.core import validators

class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = ['judul','penulis','penerbit','kelompok_id','jumlah','harga'] # tampilkan field tertentu saja
        widgets = {
            'judul': forms.TextInput({'class':'form-control', 'placeholder':"Judul"}),
            'penulis': forms.TextInput({'class':'form-control', 'placeholder':"Penulis"}),
            'penerbit': forms.TextInput({'class':'form-control', 'placeholder':"Penerbit"}),
            'kelompok_id': forms.Select({'class':'form-control', 'placeholder':"Kelompok"}),
            'jumlah': forms.NumberInput({'class':'form-control', 'placeholder':"Jumlah"}),
            'harga': forms.NumberInput({'class':'form-control', 'placeholder':"Harga"}),
        }

class FormKelompok(ModelForm):
    class Meta:
        model = Kelompok
        fields = '__all__' # tampilkan semua field 
        widgets = {
            'nama': forms.TextInput({'class':'form-control'}),
            'keterangan': forms.Textarea({'class':'form-control'}),
        }
        
class FormCustomer(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__' # tampilkan semua field 
        widgets = {
            'nama': forms.TextInput({'class':'form-control'}),
            'no_hp': forms.TextInput({'class':'form-control'}),
        }
        
class FormTransaksi(ModelForm):
    class Meta:
        model = Transaksi
        fields = '__all__' # tampilkan semua field 
        widgets = {
            'customer_id': forms.Select({'class':'form-control', 'placeholder':"Customer"}),
            'buku_id': forms.Select({'class':'form-control', 'placeholder':"Buku"}),
            'jumlah': forms.NumberInput({'class':'form-control', 'placeholder':"Jumlah"}),
            'harga': forms.NumberInput({'class':'form-control', 'placeholder':"Harga"}),
            'total_harga': forms.NumberInput({'class':'form-control', 'placeholder':"Total Harga"}),
        }
        
class SlugField(CharField):
    default_validators = [validators.validate_slug]