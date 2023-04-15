from django.db import models

# Create your models here.

class Kelompok(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

class Buku(models.Model):
    judul = models.CharField(max_length=50)
    penulis = models.CharField(max_length=40)
    penerbit = models.CharField(max_length=40)
    jumlah = models.IntegerField(null=False, default=0)
    harga = models.IntegerField(null=False, default=0)
    kelompok_id = models.ForeignKey(Kelompok, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.judul
    
class Customer(models.Model):
    nama = models.CharField(max_length=50, null=False)
    no_hp = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return self.nama
    
class Transaksi(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    buku_id = models.ForeignKey(Buku, on_delete=models.CASCADE, null=True)
    jumlah = models.IntegerField(null=True)
    harga = models.IntegerField(null=False)
    total_harga = models.IntegerField(null=False)
    
    def __str__(self):
        return self.customer_id