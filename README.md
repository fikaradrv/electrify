# Tugas 2 PBP Fikar Hilmi Adhrevi 2306203873
### Cara saya mengimplementasikan checklist
**1. Membuat sebuah proyek Django baru**
Pertama yang saya lakukan adalah membuat direktori baru dengan nama electrify dan masuk ke dalamnya, lalu di dalam direktori tersebut saya menyalakan virtual environment setelah itu di dalam direktori yang sama saya membuat berkas requirements.txt yang berisi dependencies yang perlu diinstall. setelah file requirements tersebut saya buat saya melakukan pip install -r requirements.txt pada cmd. setelah itu saya menjalankan django-admin startproject electrify . untuk membuat projek Django baru bernama electrify

**2. Membuat aplikasi dengan nama main pada proyek tersebut.**
Saya menjalankan python manage.py startapp main. Setelah perintah di atas dijalankan, direktori baru dengan nama main akan terbentuk.

**3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**
Pada direktori proyek electrify, pada berkas settings.py saya menambahkan 'main' pada INSTALLED_APPS sehingga menjadi 

'''
INSTALLED_APPS = [
    ...,
    'main'
]
'''

**4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.**
pada app main pada berkas models.py saya menambahkan 

'''
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    rating = models.IntegerField()
'''

setelah itu saya melakukan migrasi agar django dapat melacak perubahan pada model basis data yang kita miliki

**5.Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.**
Di dalam direktori main saya membuka views.py lalu saya isi dengan 

'''
from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306203873',
        'name': 'Fikar Hilmi Adhrevi',
        'class': 'PBP C'
    }
    return render(request, "main.html", context)
'''
Fungsi ini bertugas untuk menangani permintaan HTTP dan mengembalikan tampilan yang sesuai dengan context yang nantinya akan digunakan pada html.

**5. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py**

Di dalam direktori main saya membuat berkas baru bernama urls.py yang berisi

'''
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
'''

kode ini berfungsi mengatur rute URL yang terkait dengan aplikasi main. selanjutnya kita akan menambahkan rute url dalam urls.py proyek untuk menghubungkannya dengan main. pada berkas urls.py pada direktori proyek electrify saya menambahkan impor fungsi include lalu menambahkan pada url patterns menjadi

'''
urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
]
'''
urls.py ini berfungsi untuk mengatur rute url tingkat proyek

**6.Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses melalui Internet.**
Pada web PWS saya membuat project baru bernama electrify lalu pada settings.py di projek saya menambahkan URL deployment PWS pada ALLOWED_HOSTS sehingga menjadi

'''
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "fikar-hilmi-electrify.pbp.cs.ui.ac.id"]
'''
setelah itu saya menjalankan command yang diberikan pada web pws

**7. Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.**
Untuk membuat sebuah readme saya membuatnya pada notepad lalu saya save dalam bentuk file .md lalu saya add commit push pada repositori GitHub saya.

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

		http request-->		urls.py
					   |
					   |
models.py <--- read/write data --->    views.py ---> HTTP Response
					   |
					   |
					template
					filename.html

urls.py ---> nentuin URL sesuai dengan request
views.py ---> jalanin logika untuk menangani request, meminta data dari models.py
models.py ---> memberi data ke views.py
file html ---> setelah data diproses pada views dikirim ke template html untuk dirender dan ditampilkan kepada user

### Jelaskan fungsi git dalam pengembangan perangkat lunak

Git berfungsi untuk kontrol yang membantu developer untuk melacak perubahan kode, kolaborasi, dan mengelola proyek. dengan menggunakan git developer dapat dengan mudah mengelola kode yang akan ditambah atau diremove. Dengan git juga developer dapat bekerja pada branch yang berbeda, menggabungkan kode, dan recovery versi sebelumnya jika diperlukan.

### Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak
Untuk orang yang baru belajar dalam pembuatan web, Django mudah untuk dipelajari karena menggunakan arsitektur MVT sehingga memudahkan organisasi kode. Django sendiri menggunakan Bahasa python yang relatif lebih mudah dan sudah dipelajari pada DDP-1

### Mengapa model pada Django disebut sebagai ORM?
ORM sendiri adalah Object-Relational Mapping. Django disebut ORM karen Django menghubungkan objek-objek didalam kode python dengan basis data. contohnya pada tugas ini kita membuat model data pada models.py, lalu mengambil data tersebut yang akan diupdate kepada view/tampilan. 


	      



```
git status
git add
git commit
```















