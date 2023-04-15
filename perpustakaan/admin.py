from django.contrib import admin
from perpustakaan.models import Buku, Kelompok, Customer

# Register your models here.

class BukuAdmin(admin.ModelAdmin):
    list_display = ['judul','penulis','kelompok_id','jumlah']
    search_fields = ['judul','penulis','penerbit']
    list_filter = ('kelompok_id',)
    list_per_page = 4
    
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['nama']
    search_fields = ['nama']
    list_per_page = 4
    

admin.site.register(Buku, BukuAdmin)
admin.site.register(Kelompok)
admin.site.register(Customer,CustomerAdmin)