# Electrify
- Nama : Fikar Hilmi Adhrevi
- NPM : 2306203873
- Kelas : PBP C
- Link : http://fikar-hilmi-electrify.pbp.cs.ui.ac.id/

<details>
  <summary style="font-size: 30px; font-family: Arial, sans-serif;"><b>Tugas 2</b></summary>

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
</details>

<details>
  <summary style="font-size: 30px; font-family: Arial, sans-serif;"><b>Tugas 3</b></summary>

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
</details>

<details>
  <summary style="font-size: 30px; font-family: Arial, sans-serif;"><b>Tugas 4</b></summary>

### Apa perbedaan antara HttpResponseRedirect() dan redirect()

`HttpResponseRedirect()` dan  `redirect()` adalah dua cara dalam `Django` untuk melakukan `redirect()`, perbedaan dari keduanya adalah sebagai berikut:
- `redirect()` dapat menerima argumen lain selain URL seperti view name atau model object, sedangkan `HttpResponseRedirect()` hanya bisa menerima URL.
- `redirect()` dapat menggunakan fungsi `reverse()` untuk membangun URL dari view name.

### Jelaskan cara kerja penghubungan model Product dengan User!

Untuk menghubungkan model dari `Product` dengan `User`, kita akan menggunakan `Foreign Key`. Hal ini kita lakukan agar pengguna yang sedang terotorisasi hanya melihat `Product` yang telah dibuat sendiri. Berikut adalah implementasi kodenya:

1. Pada `models.py` di subdirektori `main`, tambahkan kode berikut:
    ```python
    from django.contrib.auth.models import User
    class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        ...
    ```
    Potongan kode di atas berfungsi untuk menghubungkan satu `product` dengan satu `user` melalui sebuah relationship.
    
2. Pada subdirektori `main`, buka `views.py`, dan ubah kode pada fungsi `create_product_entry`:
    ```python
    def create_product_entry(request):
        form = ProductEntryForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            product_entry = form.save(commit=False)
            product_entry.user = request.user
            product_entry.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_product_entry.html", context)
    ```
    Parameter `commit=False` yang digunakan pada potongan kode di atas berguna untuk mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari form langsung ke database. Hal tersebut memungkinkan kita untuk memodifikasi terlebih dahulu objek tersebut sebelum disimpan ke database.

3. Ubah value `product_entries` dan `context` pada fungsi `show_main` menjadi seperti berikut:
    ```python
    def show_main(request):
        product_entries = Product.objects.filter(user=request.user)
        context = {
            ...
            'name': request.user.username,
            ...
        }
        return render(request, 'main.html', context)
    ```

4. Lakukan migrations.

### Apa perbedaan antara authentication dan authorization, dan apa yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

- **Authentication** adalah proses untuk memverifikasi identitas user. Proses ini untuk memastikan bahwa user yang mencoba mengakses adalah user yang benar. Untuk implementasinya pada Django, kita akan membuat dua fitur yaitu registrasi dan login. Implementasinya dapat dilihat pada `views.py` seperti berikut:
    ```python
    def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')

        context = {'form': form}
        return render(request, 'register.html', context)
    ```

    ```python
    def login_user(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)

            if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response

        else:
            form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)
    ```

    Lalu kita akan membuat dua file HTML baru pada folder templates yang ada di `main` untuk register dan login sebagai berikut.

    `login.html`
    ```html
    {% extends 'base.html' %}

    {% block meta %}
    <title>Login</title>
    {% endblock meta %}

    {% block content %}
    <div class="login">
        <h1>Login</h1>
        <form method="POST" action="">
            {% csrf_token %}
            <table>
                {{ form.as_table }}
                <tr>
                    <td></td>
                    <td><input class="btn login_btn" type="submit" value="Login" /></td>
                </tr>
            </table>
        </form>

        {% if messages %}
        <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
        </ul>
        {% endif %}
        Don't have an account yet?
        <a href="{% url 'main:register' %}">Register Now</a>
    </div>

    {% endblock content %}
    ```

    `register.html`
    ```html
    {% extends 'base.html' %}

    {% block meta %}
    <title>Register</title>
    {% endblock meta %}

    {% block content %}
    <div class="login">
        <h1>Register</h1>

        <form method="POST">
            {% csrf_token %}
            <table>
                {{ form.as_table }}
                <tr>
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar" /></td>
                </tr>
            </table>
        </form>

        {% if messages %}
        <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
        </ul>
        {% endif %}
    </div>

    {% endblock content %}
    ```

- **Authorization** adalah proses untuk menentukan apa yang dapat dilakukan user setelah proses Authentication selesai. Berikut adalah implementasinya pada Django:
    - Untuk Authorization dalam Django, contoh implementasinya adalah penggunaan dekorator seperti `@login_required`.
    - Django juga menyediakan pembatasan akses berbasis grup atau peran pengguna.

### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

- Django dapat mengingat pengguna yang telah login dengan cara membuat session baru, session ini menyimpan informasi tentang pengguna. Setelah Django membuat sesi baru, Django mengirimkan `cookie` ke browser. `Cookie` ini akan berisi ID session yang unik yang digunakan untuk mengidentifikasi session user. Ketika pengguna logout, Django akan otomatis menghapus sesi yang dibuat tadi yang juga akan menghapus `cookie` yang dibuat.

- Kegunaan lain `cookies` adalah sebagai berikut:
    1. Pengaturan Preferensi: `Cookies` dapat menyimpan preferensi pengguna seperti bahasa atau tema.
    2. Tracking: `Cookies` juga sering digunakan untuk melacak aktivitas user di web, yang berguna untuk analitik.

- Tidak semua cookies aman untuk digunakan. Ada beberapa aspek yang perlu diperhatikan mengenai keamanan cookies:
    1. Cookies Sesi dan Cookies Persisten: Cookies sesi hanya berlaku selama sesi aktif dan akan hilang saat browser ditutup. Cookies persisten tetap ada di device user sampai waktu yang ditentukan atau dihapus secara manual, sehingga dapat menimbulkan risiko jika informasi sensitif disimpan.
    2. Cookies HTTP dan Cookies Secure: Cookies HTTP dapat diakses oleh JavaScript, sehingga rentan terhadap serangan XSS (Cross-Site Scripting). Cookies yang ditandai dengan atribut Secure hanya akan dikirim melalui koneksi HTTPS.
    3. Atribut SameSite: Menambahkan atribut SameSite dapat membantu melindungi cookies dari serangan CSRF (Cross-Site Request Forgery) dengan membatasi pengiriman cookie hanya pada permintaan dari situs yang sama.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

- Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
    1. Untuk mengimplementasikan registrasi, tambahkan fungsi pada `views.py`:
        ```python
        def register(request):
            form = UserCreationForm()

            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Your account has been successfully created!')
                    return redirect('main:login')

            context = {'form': form}
            return render(request, 'register.html', context)
        ```

        Tambahkan file `register.html` pada templates:
        ```html
        {% extends 'base.html' %}

        {% block meta %}
        <title>Register</title>
        {% endblock meta %}

        {% block content %}
        <div class="login">
            <h1>Register</h1>

            <form method="POST">
                {% csrf_token %}
                <table>
                    {{ form.as_table }}
                    <tr>
                        <td></td>
                        <td><input type="submit" name="submit" value="Daftar" /></td>
                    </tr>
                </table>
            </form>

            {% if messages %}
            <ul>
                {% for message in messages %}
                <li>{{ message }}</li>
                {% endfor %}
            </ul>
            {% endif %}
        </div>

        {% endblock content %}
        ```

        Lalu tambahkan path URL-nya pada file `urls.py` di folder `main`:
        ```python
        urlpatterns = [
            ...,
            path('register/', register, name='register'),
        ]
        ```

    2. Untuk login, tambahkan fungsi pada `views.py`:
        ```python
        def login_user(request):
            if request.method == 'POST':
                form = AuthenticationForm(data=request.POST)

                if form.is_valid():
                    user = form.get_user()
                    login(request, user)
                    response = HttpResponseRedirect(reverse("main:show_main"))
                    response.set_cookie('last_login', str(datetime.datetime.now()))
                    return response
            else:
                form = AuthenticationForm(request)

            context = {'form': form}
            return render(request, 'login.html', context)
        ```

        Buat file `login.html`:
        ```html
        {% extends 'base.html' %}

        {% block meta %}
        <title>Login</title>
        {% endblock meta %}

        {% block content %}
        <div class="login">
            <h1>Login</h1>

            <form method="POST" action="">
                {% csrf_token %}
                <table>
                    {{ form.as_table }}
                    <tr>
                        <td></td>
                        <td><input class="btn login_btn" type="submit" value="Login" /></td>
                    </tr>
                </table>
            </form>

            {% if messages %}
            <ul>
                {% for message in messages %}
                <li>{{ message }}</li>
                {% endfor %}
            </ul>
            {% endif %}
            Don't have an account yet?
            <a href="{% url 'main:register' %}">Register Now</a>
        </div>

        {% endblock content %}
        ```

        Tambahkan path URL-nya:
        ```python
        urlpatterns = [
            ...,
            path('login/', login_user, name='login'),
        ]
        ```

    3. Untuk logout, tambahkan fungsi di `views.py`:
        ```python
        def logout_user(request):
            response = HttpResponseRedirect(reverse('main:login'))
            response.delete_cookie('last_login')
            logout(request)
            return redirect('main:login')
        ```

        Buat button di `main.html` untuk memanggil fungsi logout:
        ```html
        <a href="{% url 'main:logout' %}">
            <button class="logout-button">Logout</button>
        </a>
        ```

- Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
    ![dummy1](https://github.com/user-attachments/assets/23cf0d11-12ef-4d1e-86ad-3dc2a63abaaf)
    ![image](https://github.com/user-attachments/assets/1113a0a6-2fb0-4f7a-868d-0b3831fa64ef)

- Menghubungkan model Product dengan User. Implementasinya adalah dengan menggunakan `ForeignKey` seperti berikut:
    ```python
    from django.contrib.auth.models import User
    class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        ...
    ```

- Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi. Untuk mengimplementasikan detail last login dan menampilkan cookies, gunakan kode berikut:
    ```python
    def show_main(request):
        ...
        context = {
            ...
            'name': request.user.username,
            'last_login': request.COOKIES['last_login'],
        }
        return render(request, 'main.html', context)
    ```
    ![image](https://github.com/user-attachments/assets/f5f12990-7543-4f57-b6ca-a60b3e5c3ddf)
</details>

<details>
  <summary style="font-size: 30px; font-family: Arial, sans-serif;"><b>Tugas 5</b></summary>

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Terdapat 4 elemen selector pada CSS yaitu Inline Styles, ID Selector, Class Selector, dan Element Selector. Berikut adalah prioritasnya.
1. Inline Styles : Inline style adalah penggunaan css untuk memberikan style untuk satu elemen. Contoh :
    ```html
    <div style="color: red;">Hello World</div>
    ```
2. ID selector : ID Selector adalah salah satu selector yang penggunaanya menggunakan id elemen. Contoh:
    ```css
    #header {
    color: blue;
    }
    ```
3. Class Selector : Class Selector adalah Selector yang menggunakan class `.class`, atribut `type="text"`, atau pseudo-class `:hover`. Contoh :
    ```css
    .button {
        color: green;
    }
    ```
4. Element Selector : Selector yang menggunakan nama elemen HTML `div`, `h1`, dll. dan pseudo-element `::before`, `::after`. Contoh :
    ```css
    * {
    color: gray;
    }
    ```

    Jika dua atau lebih selector memiliki spesifisitas yang sama, urutan di mana mereka dituliskan dalam stylesheet juga mempengaruhi. Selector yang ditulis terakhir akan diterapkan.

### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

Responsive design adalah pendekatan dalam web development dimana tampilan web dapat menyesuaikan dengan berbagai ukuran layar perangkat (desktop, tablet, dan smartphone).

**Mengapa Penting** :
- Pengalaman User: Dengan responsive design, user akan mendapatkan pengalaman yang konsisten dan optimal di berbagai perangkat. hal ini agar dapat meningkatkan kepuasan user.
- SEO : SEO atau Search Engine Optimalization adalah bagaimana sebuah search engine meranking sebuah search page dalam search enginenya. Google memprioritaskan situs web yang pada designnya menggunakan responsive design. Sehingga dengan menggunakan responsive design akan meningkatkan ranking SEO pada web
- Penghematan Biaya dan Waktu: Dengan menggunakan responsive design akan mengurangi kebutuhan untuk membuat dan memelihara versi terpisah dari web untuk perangkat yang berbeda.

Contoh aplikasi yang menggunakan responsive design:
1. Twitter
2. Tokopedia

Contoh aplikasi yang tidak menggunakan responsive design:
Beberapa situs lama yang sudah outdated. Untuk sekarang jarang ditemukan aplikasi yuang tidak menggunakan responsive design

### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
**1. Margin**
- Definisi: Margin adalah ruang kosong di luar elemen HTML. Margin digunakan untuk memberikan jarak antara elemen dan elemen lainnya di sekitarnya.
- Implementasi:
    ```css
    .element {
        margin: 20px;
    }
    ```
**2. Border**
- Definisi: Border adalah garis yang mengelilingi elemen HTML. Border bisa berwarna, bold, dan memiliki style (solid, dashed, dll).
- Implementasi:
    ```css
    .element {
        border: 2px solid black; 
    }
    ```
**3. Padding**
- Definisi: Padding adalah ruang kosong di dalam elemen HTML, antara konten (seperti teks atau gambar) dan border elemen tersebut. Padding memberikan ruang antara konten dan batas elemen.
- **Implementasi**:
    ```css
    .element {
        padding: 15px;
    }
    ```
### Jelaskan konsep flex box dan grid layout beserta kegunaannya!
**1. Flexbox**
- Definisi: Flexbox, atau Flexible Box Layout, adalah cara untuk mengatur elemen di dalam satu baris atau kolom. flex box membantu dalam mendistribusikan ruang dan meratakan elemen dengan mudah.
- Kapan Digunakan: Flexbox digunakan ketika ingin mengatur elemen dalam satu arah (baris atau kolom) dan ingin memastikan elemen tersebut dapat membesar atau mengecil sesuai dengan ukuran kontainer.
- Implementasi:
    ```css
    .container {
        display: flex; 
        justify-content: space-between; 
        align-items: center; 
    }
    ```

**2. Grid Layout**
- Definisi: Grid Layout adalah cara untuk mengatur elemen dalam baris dan kolom. Grid Layout memungkinkan kita untuk membuat tata letak yang lebih kompleks dan terstruktur.
- Kapan Digunakan: Grid Layout digunakan ketika kita ingin mengatur elemen dalam dua dimensi (baik baris dan kolom) dan memerlukan kontrol yang lebih besar atas posisi elemen.
- Implementasi:
    ```css
    .container {
        display: grid;
        grid-template-columns: repeat(3, 1fr); 
        gap: 10px; 
    }
    ```

**Kesimpulan**
- **Flexbox**: Baik digunakan untuk layout satu dimensi (baris atau kolom). Mudah digunakan untuk meratakan dan mendistribusikan elemen.
- **Grid Layout**: Baik digunakan untuk layout dua dimensi (baris dan kolom). Memberikan kontrol lebih besar untuk tata letak yang kompleks.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

1. **Implementasikan fungsi untuk menghapus dan mengedit product.**
    Untuk mengedit dan menghapus product, saya membuat dua fungsi baru di `views.py` yaitu `edit_product` dan `delete_product`.
    ```python
    def edit_product(request, id):
    product = Product.objects.get(pk = id)

    form = ProductEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

    def delete_product(request, id):
        product = Product.objects.get(pk = id)
        product.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
    ```
    Selanjutnya saya buat file html baru yaitu `edit_product.html` yang akan berfungsi untuk template edit product. Setelah itu saya buat path urlnya di `urls.py` dengan mengimport fungsi `edit_product` dan `delete_product` dan menambahkan pathnya sebagai berikut:
    ```python
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),
    ```
2. **Kustomisasi halaman login, register, dan tambah product semenarik mungkin.**
    Tampilan `login.html` saya edit menggunakan Tailwind CSS dengan penjelasan sebagai berikut:

    1. Memakai flex dan grid agar sesuai berbagai ukuran layar.
    2. Warna: Kombinasi kuning dan biru.
    3. Memberikan Efek Shadow pada kotak utama.
    4. Tombol diwarnai kuning dan hover menjadi kuning lebih gelap.
    5. Pesan berwarna biru, hijau, dan merah sesuai jenis pesannya.
    
    Tampilan `register.html` saya edit menggunakan Tailwind CSS dengan penjelasan sebagai berikut:
    1. Menggunakan flex untuk layout responsif.
    2. Warna menggunakan kuning dan biru sesuai tema.
    3. Efek shadow pada kotak utama untuk dimensi visual.
    4. Tombol daftar berwarna kuning dengan efek hover.
    5. Pesan error ditampilkan dengan warna merah.
    6. Input fields dengan focus states yang jelas.
    7. Layout form yang rapi dengan spacing konsisten.
    8. Link "Login di sini" berwarna biru dengan efek hover.

    Tampilan `create_product_entry.html` saya edit menggunakan Tailwind CSS dengan penjelasan sebagai berikut:
    1. Layout responsif dengan flex dan min-h-screen untuk mengisi seluruh tinggi layar.
    2. Warna latar belakang abu-abu muda dengan form putih untuk kontras.
    3. Form dalam kotak putih dengan bayangan dan sudut membulat.
    4. Input fields dengan label jelas dan pesan error merah.
    5. Tombol submit kuning dengan efek hover.
    6. Spacing konsisten antar elemen form.
    7. Desain responsif dengan padding dan margin yang sesuai.

3. **Kustomisasi halaman daftar product menjadi lebih menarik dan responsive.**
    Untuk bikin halaman daftar produk kita menjadi lebih menarik dan bisa nyesuain di berbagai ukuran layar, saya edit `main.html` dan `card_product.html`. Berikut penjelasan saya:

   1. Layout yang Fleksibel:
      - Pake Flexbox buat ngatur konten (`flex flex-col items-center`). Jadi semuanya rapi ke tengah.
      - Produknya ditata pake grid yang bisa berubah-ubah (`grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6`). Di HP cuma 1 kolom, di tablet 2, di laptop 3.
      - Kasih padding yang pinter (`px-4 md:px-8`). Jadi di HP nggak terlalu mepet, di layar gede lebih lega.

   2. Tampilan:
      - Background halaman abu-abu muda (`bg-gray-100`).
      - Judul "Product List" dikasih background kuning tua (`bg-yellow-600`).
      - Kartu produk punya border kuning (`border-2 border-yellow-500`) dan bayangan (`shadow-md`).

   3. Kalau Belum Ada Produk:
      - Nunjukin gambar "no-products.png" sama pesan.
      - Pake Flexbox buat naruh semuanya di tengah-tengah (`flex flex-col items-center justify-center`).
      - Kasih tinggi minimum (`min-h-[24rem]`) biar nggak keliatan kosong banget.

   4. Kalau Udah Ada Produk:
      - Produknya ditampilin dalam grid yang bisa nyesuain.
      - Tiap produk pake komponen `card_product.html`.
      - Kartu produk isinya info penting: nama, harga, stok, deskripsi, sama rating.
      - Ada tombol edit dan delete dengan ikon dari static.

4. **Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut**

    Untuk setiap kartu produk, saya nambahin dua tombol di bagian bawahnya:

    1. Tombol Edit:
    - Bentuknya ikon pensil.
    - Kalau diklik, langsung ngarahin ke halaman edit produk.

    2. Tombol Delete:
    - Ikon tempat sampah.
    - Sekali klik, produknya langsung hilang dari daftar.

    Kedua tombol ini dibikin pake tag `<a>` yang dihias pake Tailwind CSS. Ikonnya diambil dari folder static, jadi bisa gampang diganti.
5. **Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.**
    Buat bikin navbar yang responsive, saya bikin file `navbar.html` pake Tailwind CSS. Nih, berikut penjelasan saya:

    1. Struktur Utama:
    - Pake tag `<nav>` buat wrap semuanya. Dikasih kelas `fixed top-0 left-0 right-0` biar nempel terus di atas.
    - Warnanya kuning (`bg-yellow-500`) dan ada bayangannya (`shadow-md`).

    2. Biar Bisa Nyesuain Layar:
    - Pake Flexbox (`flex items-center justify-between`) buat ngatur isinya.
    - Di HP, menunya disembunyiin, gantinya ada tombol hamburger
    - Di laptop atau PC, menunya langsung keliatan semua.

    3. Logo sama Judul:
    - Logo "Electrify" ditaro di kiri, ukurannya bisa gede-kecil tergantung layar.
    - Pake `text-2xl md:text-3xl` biar di HP nggak kegedean, di laptop pas.

    4. Menu Navigasinya:
    - Menu utamanya (`<ul>`) dikasih `hidden md:flex`. Jadi di HP ilang, di laptop nongol.
    - Tiap menu (`<li>`) dikasih jarak dan efek hover.

    5. Tombol Hamburger:
    - Cuma nongol di HP, pake `md:hidden`.
    - Gambarnya pake SVG, jadi nggak pecah-pecah.

    6. Menu buat HP:
    - Awalnya disembunyiin, baru muncul kalo tombol hamburger dipencet.
    - Posisinya tepat di bawah navbar pake `absolute top-full left-0 right-0`.
    - Warnanya putih biar keliatan jelas bedanya sama navbar.

</details>

<details>
  <summary style="font-size: 30px; font-family: Arial, sans-serif;"><b>Tugas 6</b></summary>
  
### Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!

Penggunaan JavaScript dalam pengembangan aplikasi web, khususnya dalam konteks proyek Electrify, memberikan beberapa manfaat penting:

1. Interaktivitas: JavaScript memungkinkan pembuatan elemen interaktif pada halaman web. Dalam proyek ini terlihat pada implementasi modal untuk menambahkan produk dan fungsi-fungsi seperti `showModal()` dan `hideModal()`.


2. Dinamisme: Dengan JavaScript, konten halaman dapat diperbarui secara dinamis tanpa perlu me-refresh seluruh halaman. Fungsi `refreshProductEntries()` di proyek ini contohnya adalah dengan memperbarui daftar produk secara real-time.

3. Asynchronous Operations: JavaScript memungkinkan operasi asynchronous, yang penting untuk komunikasi dengan server tanpa menghentikan eksekusi kode lainnya. Penggunaan `fetch()` di proyek ini untuk mengambil dan mengirim data produk.

4. Validasi Form: JavaScript dapat digunakan untuk memvalidasi input pengguna sebelum dikirim ke server, meningkatkan user experience dan mengurangi beban server. 

5. Manipulasi DOM: JavaScript memungkinkan manipulasi struktur, gaya, dan konten halaman web secara dinamis. di proyek ini terlihat saat menambahkan atau menghapus elemen produk dari DOM.

6. Responsif UI: Dengan JavaScript, kita dapat membuat antarmuka pengguna yang responsif terhadap interaksi pengguna. Contohnya adalah implementasi navbar responsif di proyek ini yang menyesuaikan tampilan berdasarkan ukuran layar.

7. AJAX: JavaScript memungkinkan komunikasi asynchronous dengan server melalui AJAX, yang digunakan di proyek ini yaitu untuk menambahkan produk tanpa me-refresh halaman (`addProductEntry()`).

Penggunaan JavaScript dalam proyek ini meningkatkan interaktivitas, kinerja, dan pengalaman pengguna secara keseluruhan, membuat aplikasi web lebih dinamis dan responsif.

### Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?

Penggunaan `await` dengan `fetch()` di proyek ini berfungsi untuk menunggu resolusi Promise yang dikembalikan oleh `fetch()` sebelum melanjutkan eksekusi kode. Ini penting karena:

1. Sinkronisasi: `await` memastikan bahwa kode menunggu sampai data dari server diterima sebelum melanjutkan, menjaga urutan eksekusi yang benar.

2. Penanganan Error: Memudahkan penanganan error dengan memungkinkan penggunaan blok try-catch untuk menangkap kesalahan dalam operasi asynchronous.

3. Readability: Membuat kode asynchronous lebih mudah dibaca dan dipahami, mirip dengan kode synchronous.

Dalam Electrify, `await` digunakan dalam fungsi `getProductEntries()`:
```
async function getProductEntries() {
    const response = await fetch("{% url 'main:show_json' %}");
    return await response.json();
}
```

Jika `await` tidak digunakan:

1. Asynchronous Execution: Kode akan terus berjalan tanpa menunggu `fetch()` selesai, yang dapat menyebabkan kesalahan jika mencoba mengakses data yang belum tersedia.

2. Penanganan Promise: Kita harus menggunakan `.then()` untuk menangani hasil `fetch()`, yang dapat membuat kode lebih kompleks, terutama untuk operasi berurutan.

3. Error Handling: Penanganan error menjadi lebih rumit karena kita perlu menggunakan `.catch()` terpisah untuk setiap Promise.

### Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?

Decorator `csrf_exempt` digunakan pada view yang menangani AJAX POST request untuk menonaktifkan perlindungan CSRF (Cross-Site Request Forgery) Django. Alasannya:

1. AJAX Request: AJAX request sering tidak menyertakan CSRF token yang biasanya disertakan dalam form HTML.

2. Keamanan vs Kemudahan: Dalam beberapa kasus, seperti API publik atau endpoint yang tidak memerlukan autentikasi, perlindungan CSRF mungkin tidak diperlukan atau bahkan menghambat fungsionalitas.

3. Alternatif Keamanan: Ketika `csrf_exempt` digunakan, penting untuk menerapkan metode keamanan alternatif seperti autentikasi token.

Dalam proyek ini, `csrf_exempt` digunakan pada view `add_product_ajax`:

```
@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        user = request.user

        new_product = Product(name=name, price=price, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```

### Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

Pembersihan data input pengguna dilakukan di backend selain di frontend karena:

1. Keamanan Berlapis: Validasi di frontend bisa dilewati oleh user yang mahir, sehingga validasi di backend menjadi lapisan keamanan tambahan.

2. Konsistensi Data: Backend memastikan bahwa semua data yang masuk ke database telah dibersihkan, terlepas dari sumber inputnya (web, mobile app, API).

3. Perlindungan terhadap Serangan: Backend dapat melindungi dari serangan seperti SQL Injection yang mungkin lolos dari validasi frontend.

4. Validasi Kompleks: Beberapa validasi mungkin memerlukan akses ke database atau logika bisnis yang hanya tersedia di backend.

5. Keandalan: Tidak bisa sepenuhnya mengandalkan validasi client-side karena bisa dimanipulasi oleh pengguna.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

AJAX GET

1. Mengubah kode cards data product agar dapat mendukung AJAX GET dan melakukan pengambilan data product menggunakan AJAX GET, memastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in:

   - Membuat fungsi pada views.py untuk mengembalikan data product dalam format JSON:
   
     ```python
     def show_json(request):
         data = Product.objects.filter(user=request.user)
         return HttpResponse(serializers.serialize("json", data), content_type="application/json")
     ```

   - Menambahkan URL pattern untuk fungsi show_json di urls.py.

   - Membuat fungsi JavaScript asinkron di main.html untuk mengambil data product:
   
     ```javascript
     async function getProductEntries() {
         return fetch("{% url 'main:show_json' %}").then((res) => res.json());
     }
     ```

   - Implementasi fungsi refreshProductEntries() untuk memperbarui tampilan product cards:
   
     ```javascript
     async function refreshProductEntries() {
         document.getElementById("product_entry_cards").innerHTML = "";
         document.getElementById("product_entry_cards").className = "";
         const productEntries = await getProductEntries();
         let htmlString = "";
         let classNameString = "";

         if (productEntries.length === 0) {
             classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
             htmlString = `
                 <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                     <img src="{% static 'image/no-products.png' %}" alt="No products" class="w-32 h-32 mb-4"/>
                     <p class="text-center text-gray-600 mt-4">No products available.</p>
                 </div>
             `;
         } else {
             classNameString = "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 w-full"
             productEntries.forEach((item) => {
                 htmlString += `
                 <div class="bg-white shadow-md rounded-lg border-2 border-yellow-500 mb-4">
                     <div class="p-4">
                         <h3 class="font-bold text-xl mb-2 text-yellow-500">${DOMPurify.sanitize(item.fields.name)}</h3>
                         <p class="text-gray-700"><strong>Price:</strong> Rp.${item.fields.price}</p>
                         <p class="text-gray-700"><strong>Stock:</strong> ${item.fields.stock}</p>
                         <p class="text-gray-700"><strong>Description:</strong> ${DOMPurify.sanitize(item.fields.description)}</p>
                         <p class="text-gray-700"><strong>Rating:</strong> ${item.fields.rating} Stars</p>
                     </div>
                     <div class="flex justify-between p-4 border-t border-blue-200">
                         <a href="/edit-product/${item.pk}" class="inline-flex items-center">
                             <img src="{% static 'image/edit-icon.png' %}" alt="Edit product" class="w-6 h-6" />
                         </a>
                         <a href="/delete/${item.pk}" class="inline-flex items-center">
                             <img src="{% static 'image/delete-icon.png' %}" alt="Delete product" class="w-6 h-6" />
                         </a>
                     </div>
                 </div>
                 `;
             });
         }
         document.getElementById("product_entry_cards").className = classNameString;
         document.getElementById("product_entry_cards").innerHTML = htmlString;
     }
     ```

   - Memanggil fungsi refreshProductEntries() saat halaman dimuat:
   
     ```javascript
     refreshProductEntries();
     ```

AJAX POST

2. Membuat tombol yang membuka modal dengan form untuk menambahkan product:
   - Menambahkan HTML untuk modal dan form di main.html:
     ```html
     <button data-modal-target="crudModal" data-modal-toggle="crudModal" 
             class="btn bg-yellow-500 hover:bg-yellow-600 text-white font-bold py-2 px-4 rounded-lg 
                    transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105 mb-4" 
             onclick="showModal();">
         Add New Product by AJAX
     </button>
     ```
   - Membuat fungsi JavaScript untuk menampilkan dan menyembunyikan modal:
     ```javascript
     function showModal() {
         modal.classList.remove('hidden'); 
         setTimeout(() => {
             modalContent.classList.remove('opacity-0', 'scale-95');
             modalContent.classList.add('opacity-100', 'scale-100');
         }, 50); 
     }

     function hideModal() {
         modalContent.classList.remove('opacity-100', 'scale-100');
         modalContent.classList.add('opacity-0', 'scale-95');

         setTimeout(() => {
             modal.classList.add('hidden');
         }, 150); 
     }
     ```

3. Membuat fungsi view baru untuk menambahkan product baru ke dalam basis data:
   - Implementasi fungsi add_product_ajax di views.py:
     ```python
     @csrf_exempt
     @require_POST
     def add_product_entry_ajax(request):
         name = strip_tags(request.POST.get("name"))
         price = request.POST.get("price")
         stock = request.POST.get("stock")
         description = strip_tags(request.POST.get("description"))
         rating = request.POST.get("rating")
         user = request.user

         new_product = Product(
             name=name, 
             price=price,
             stock=stock,
             description=description,
             rating=rating,
             user=user
         )
         new_product.save()

         return HttpResponse(b"CREATED", status=201)
     ```

4. Membuat path /create-ajax/ yang mengarah ke fungsi view yang baru dibuat:
   - Menambahkan URL pattern di urls.py:
     ```python
     path('create-product-entry-ajax/', add_product_entry_ajax, name='add_product_entry_ajax'),
     ```

5. Menghubungkan form di dalam modal ke path /create-ajax/:
   - Membuat fungsi JavaScript untuk mengirim data form menggunakan AJAX:
   ```javascript
     function addProductEntry() {
         fetch("{% url 'main:add_product_entry_ajax' %}", {
             method: "POST",
             body: new FormData(document.querySelector('#productEntryForm')),
         })
         .then(response => refreshProductEntries())

         document.getElementById("productEntryForm").reset(); 
         hideModal();

         return false;
     }

     document.getElementById("productEntryForm").addEventListener("submit", (e) => {
         e.preventDefault();
         addProductEntry();
     })
     ```

     

6. Melakukan refresh pada halaman utama secara asinkronus:
   - Memanggil refreshProductEntries() setelah berhasil menambahkan product baru:
     ```javascript
     function addProductEntry() {
         // ... (kode sebelumnya)
         .then(refreshProductEntries)
         // ... (kode selanjutnya)
     }
     ```












    
















