# Electrify
- Nama : Fikar Hilmi Adhrevi
- NPM : 2306203873
- Kelas : PBP C
- Link : http://fikar-hilmi-electrify.pbp.cs.ui.ac.id/

# Table of contents
- [Tugas 2](#tugas-2)


# Tugas 2
http://fikar-hilmi-electrify.pbp.cs.ui.ac.id/
### Cara saya mengimplementasikan checklist
**1. Membuat sebuah proyek Django baru**
Pertama yang saya lakukan adalah membuat direktori baru dengan nama electrify dan masuk ke dalamnya, lalu di dalam direktori tersebut saya menyalakan virtual environment setelah itu di dalam direktori yang sama saya membuat berkas requirements.txt yang berisi dependencies yang perlu diinstall. setelah file requirements tersebut saya buat saya melakukan pip install -r requirements.txt pada cmd. setelah itu saya menjalankan django-admin startproject electrify . untuk membuat projek Django baru bernama electrify

**2. Membuat aplikasi dengan nama main pada proyek tersebut.**
Saya menjalankan python manage.py startapp main. Setelah perintah di atas dijalankan, direktori baru dengan nama main akan terbentuk.

**3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**
Pada direktori proyek electrify, pada berkas settings.py saya menambahkan 'main' pada INSTALLED_APPS sehingga menjadi 

```
INSTALLED_APPS = [
    ...,
    'main'
]
```

**4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.**
pada app main pada berkas models.py saya menambahkan 

```
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    rating = models.IntegerField()
```

setelah itu saya melakukan migrasi agar django dapat melacak perubahan pada model basis data yang kita miliki

**5.Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.**
Di dalam direktori main saya membuka views.py lalu saya isi dengan 

```
from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306203873',
        'name': 'Fikar Hilmi Adhrevi',
        'class': 'PBP C'
    }
    return render(request, "main.html", context)
```
Fungsi ini bertugas untuk menangani permintaan HTTP dan mengembalikan tampilan yang sesuai dengan context yang nantinya akan digunakan pada html.

**5. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py**

Di dalam direktori main saya membuat berkas baru bernama urls.py yang berisi

```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

kode ini berfungsi mengatur rute URL yang terkait dengan aplikasi main. selanjutnya kita akan menambahkan rute url dalam urls.py proyek untuk menghubungkannya dengan main. pada berkas urls.py pada direktori proyek electrify saya menambahkan impor fungsi include lalu menambahkan pada url patterns menjadi

```
urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
]
```
urls.py ini berfungsi untuk mengatur rute url tingkat proyek

**6.Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses melalui Internet.**
Pada web PWS saya membuat project baru bernama electrify lalu pada settings.py di projek saya menambahkan URL deployment PWS pada ALLOWED_HOSTS sehingga menjadi

```
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "fikar-hilmi-electrify.pbp.cs.ui.ac.id"]
```
setelah itu saya menjalankan command yang diberikan pada web pws

**7. Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.**
Untuk membuat sebuah readme saya membuatnya pada notepad lalu saya save dalam bentuk file .md lalu saya add commit push pada repositori GitHub saya.

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Screenshot 2024-09-09 155824](https://github.com/user-attachments/assets/7338e963-d138-49f2-8f75-224083b2393d)


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

# Tugas 3

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Setelah membaca beberapa referensi, menurut saya **data delivery** diperlukan untuk memastikan bahwa data yang diproses di server dan database dapat berinteraksi dengan user.

Dalam konteks tugas ini adalah ketika user ingin melihat produk apa saja yang ada di platform. Agar platform dapat menampilkan produk-produk tersebut ke user, maka platform harus melakukan **data delivery** dari database ke frontend yang akan ditampilkan kepada user.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Setelah membaca beberapa referensi, saya mendapat kesimpulan bahwa JSON lebih baik digunakan dibandingkan XML karena beberapa alasan berikut: 
- JSON memiliki struktur yang lebih mudah untuk dibaca oleh manusia dibandingkan XML
- JSON memiliki ukuran data yang lebih *lightweight* dibandingkan XML. Hal ini dikarenakan JSON tidak memerlukan tag pembuka dan penutup seperti XML
- JSON sendiri lebih kompatibel secara langsung dengan JavaScript karena JSON sendiri adalah subset dari Syntax JavaScript. Karena hal ini JSON lebih mudah untuk di *Parsing*, manipulasi, dan digunakan pada aplikasi JavaScript

Karena alasan diataslah juga yang menyebabkan JSON lebih populer untuk digunakan dibandingkan XML

### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method `is_valid()` pada form Django berfungsi untuk memeriksa apakah data yang dimasukkan ke dalam form memenuhi semua aturan validasi yang telah ditentukan. Jika data valid, method ini akan mengembalikan nilai `True` , sedangkan jika ada kesalahan dalam data, akan mengembalikan `False` dan mengisi atribut errors dengan pesan kesalahan. Method ini penting karena memastikan bahwa data yang diterima dan diproses dari form sudah sesuai dengan format yang diharapkan, mencegah kesalahan input atau data yang tidak valid.

### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

`csrf_token` diperlukan dalam pembuatan form di Django untuk melindungi platform dari serangan Cross-Site Request Forgery (CSRF). Tanpa token ini, seorang penyerang dapat mengeksploitasi sesi pengguna dengan membuat permintaan yang tidak sah, seperti memalsukan data atau menjalankan tindakan tanpa izin. `csrf_token` memastikan bahwa hanya permintaan yang sah dari situs yang dapat diproses oleh server, sehingga mencegah tindakan berbahaya yang dilakukan atas nama pengguna tanpa sepengetahuan mereka.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

**1. Membuat input `form` untuk menambahkan objek model pada app sebelumnya.**

- Yang pertama saya lakukan adalah membuat file `forms.py` pada direktori `main`. `forms.py` ini akan berfungsi untuk menerima data sesuai model yang dimiliki. isi dari `forms.py` akan seperti dibawah ini

    ```
    from django.forms import ModelForm
    from main.models import Product

    class ProductEntryForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "price", "description", "stock", "rating"]
    ```

- Lalu yang saya lakukan adalah membuat perubahan pada `views.py` sehingga `forms.py` dapat diakses. pada `views.py` saya membuat fungsi baru yaitu `create_product_entry` 

    ```
    def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
    ```

    fungsi ini akan berguna untuk menghasilkan form yang dapat menambahkan data product secara otomatis ketika data di-submit dari form.

- Selanjutnya saya membuat file HTML baru pada templates di direktori main yang berguna untuk menampilkan user interface `forms.py` dengan nama `create_product_entry.html` dengan isi dibawah ini

    ```
    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add New Product</h1>

    <form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
        <td></td>
        <td>
            <input type="submit" value="Add Product" />
        </td>
        </tr>
    </table>
    </form>

    {% endblock %}
    ```

- Selanjutnya saya menambahkan path untuk `create_product_entry` pada `urls.py` dengan melakukan perubahan sebagai berikut
    ```
    from main.views import show_main, create_product_entry,
    ```
    ```
    urlpatterns = [
        ...
        path('create-product-entry', create_product_entry, name='create_product_entry'),
    ]
    ```
- Setelah itu saya memodifikasi file `main.html` di dalam `{% block content $}` sehingga dapat menampilkan halaman form. kode yang ditambahkan adalah sebagai berikut
    ```
    ...
    {% if not product_entries %}
    <p>Belum ada product pada toko ini.</p>
    {% else %}
    <table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Stock</th>
        <th>Rating</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data mood di bawah baris ini 
    {% endcomment %} 
    {% for product_entry in product_entries %}
    <tr>
        <td>{{product_entry.name}}</td>
        <td>{{product_entry.price}}</td>
        <td>{{product_entry.description}}</td>
        <td>{{product_entry.stock}}</td>
        <td>{{product_entry.rating}}</td>
    </tr>
    {% endfor %}
    </table>
    {% endif %}

    <br />

    <a href="{% url 'main:create_product_entry' %}">
    <button>Add New Product</button>
    </a>
    ```

**2. Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID dan membuat routing untuk masing masing views**

- Saya menambahkan 4 fungsi baru pada `views.py` agar dapat menampilkan data berdasarkan JSON, XML, dan by id. berikut adalah modifikasinya
    ```
    def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

- Lalu saya memodifikasi `urls.py` pada direktori main dengan mengimport fungsi dan membuat path untuk keempat fungsi yang sudah dibuat tadi
    ```
    from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
    ...
    urlpatterns = [
    ...
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'), 
    ]
    ```

### Screenshot Postman

**1. JSON**
    ![JSON](https://github.com/user-attachments/assets/a0968876-9d7c-4b29-837e-c12991e42eaf)

**2. XML**
    ![xml](https://github.com/user-attachments/assets/103dc04d-b97a-44b0-aa80-3fdd58a00fe4)

**3. JSON by ID**
    ![json by id](https://github.com/user-attachments/assets/941df5a3-ac05-4aff-99a9-62b39c7c9ed1)

**4. XML by ID**
    ![xml by id](https://github.com/user-attachments/assets/6c20f2f3-6c20-4272-bbbb-a6dc850de3e7)




	      



















