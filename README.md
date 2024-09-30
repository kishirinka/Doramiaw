
# Doramiaw E-commerce

### Nama: Irma Nia Alwijah  
### NPM: 2306226864  
### Kelas: PBP B  

[Link PWS](http://irma-nia-doramiaw.pbp.cs.ui.ac.id)

# ------ T U G A S  2 -----  

## 1. Implementasi Checklist

Untuk menyelesaikan tugas ini, saya melakukan langkah-langkah berikut:

1. **Membuat Repository GitHub**  
   Saya memulai dengan membuat repository GitHub dengan nama proyek e-commerce saya, *Doramiaw*. Kemudian saya melakukan cloning repository ke laptop agar bisa dikerjakan secara lokal. Setiap ada perubahan, saya melakukan `git add`, `git commit`, dan `git push` ke GitHub.

2. **Membuat Branch dan Mengaktifkan Environment**  
   Semua pekerjaan dilakukan di branch `main`. Saya mengaktifkan virtual environment di cmd dan membuat proyek Django bernama *Doramiaw*.

3. **Menambahkan Dependencies**  
   Saya membuat file `requirements.txt` yang berisi daftar dependencies dan menginstalnya. Saya juga menambahkan *allowed hosts* di `settings.py` agar aplikasi web dapat diakses.

4. **Membuat `.gitignore`**  
   File `.gitignore` dibuat untuk mengabaikan file yang tidak perlu dilacak oleh Git, seperti file environment dan direktori lainnya.

5. **Membuat Aplikasi Utama**  
   Saya membuat aplikasi bernama `main` di dalam proyek *Doramiaw*. Kemudian, menambahkan aplikasi tersebut di `INSTALLED_APPS` pada `settings.py`.

6. **Membuat Template HTML**  
   Dalam folder `main`, saya membuat folder `templates` yang berisi file HTML sesuai desain e-commerce saya.

7. **Mengelola Model dan Database**  
   Saya mengubah `models.py` dengan data produk yang ada di e-commerce, lalu melakukan migrasi (`makemigrations` dan `migrate`).

8. **Menghubungkan Template dengan Views**  
   Saya menambahkan logika di `views.py` dan menghubungkannya dengan template HTML. Pada `urls.py`, saya mengatur rute URL untuk aplikasi `main` dan menautkannya di `urls.py` proyek utama.

9. **Deploy ke PWS**  
   Setelah semua langkah di atas selesai, saya melakukan `push` direktori proyek ke PWS. Langkah ini saya lakukan terakhir karena PWS sempat mengalami masalah saat pengerjaan tugas.

## 2. Diagram Alur Request Client dan Response di Django

![image](https://github.com/user-attachments/assets/c90c9074-57cf-408c-a326-8778965721d4)

## 3. Fungsi Git dalam Pengembangan Perangkat Lunak

Git berfungsi sebagai sistem kontrol versi yang memungkinkan kita menyimpan, mengelola, dan melacak perubahan dalam kode. Hal ini sangat membantu saat melakukan revisi berkala dan bekerja dalam tim, karena memungkinkan kolaborasi tanpa saling mengganggu satu sama lain.

## 4. Alasan Django Dipilih untuk Belajar Pengembangan Perangkat Lunak

Django cocok untuk pemula karena menyediakan banyak fitur bawaan seperti interaksi dengan database, sistem routing, dan keamanan. Django juga memiliki struktur yang jelas dengan menggunakan pola Model-View-Template (MVT), serta dokumentasi yang lengkap dan mudah dipahami.

## 5. Mengapa Model di Django Disebut sebagai ORM

Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena berfungsi sebagai penghubung antara kode Python dan database. Melalui ORM, kita bisa membuat, membaca, memperbarui, dan menghapus data dari database tanpa menulis query SQL secara langsung. Setiap model merepresentasikan tabel di database, dan atribut di dalamnya merepresentasikan kolom-kolom tabel tersebut.


=========================================================================================================================================================================================================================================================================


# ------ T U G A S  3 -----  

## 1. Pentingnya Data Delivery dalam Pengimplementasian Platform

Dalam membuat sebuah platform, data delivery sangat penting karena memastikan informasi bisa dikirim dan diterima dengan cepat dan akurat. Data delivery diperlukan agar platform yang dibuat bisa berjalan lancar. Dalam pembuatan platform e-commerce seperti ini, data delivery sangat berguna untuk menarik kepuasan penggunanya. 

Misalnya,saat pengguna mencari produk, informasi tentang produk tersebut harus segera muncul. Jika tidak, pengguna akan merasa tidak nyaman dengan platform yang digunakan. Kecepatan dan ketepatan pengiriman data sangat berpengaruh terhadap kepuasan pengguna.

Jadi, data delivery membantu memastikan platform bisa memberikan layanan yang cepat, aman, dan bisa diandalkan, sehingga pengguna merasa nyaman dan platform saya bisa terus berkembang.

## 2. XML dan JSON
Json lebih populer pasti karena banyak alasan, salah satunya karena lebih baik dari xml. Saya sangat setuju dengan hal tersebut. JSON lebih mudah dibaca karena strukturnya simpel sehingga sehingga mudah menemukan atau memperbaiki kesalahan dalam data jika ada yang tidak sesuai. Data di JSON tidak memerlukan tag pembuka dan penutup seperti di XML, sehingga ukurannya lebih kecil dan lebih cepat untuk ditransfer.

## 3. Fungsi Method `is_valid()` dalam Form Django
Method `is_valid()` pada form Django digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form sudah benar dan sesuai dengan aturan yang ditentukan. Method ini mengecek apakah semua data yang dimasukkan oleh pengguna memenuhi semua syarat dan aturan yang telah ditentukan di form, seperti format harga barang yang benar atau panjang karakter yang sesuai. Dengan demikian, kita bisa memastikan bahwa data yang diproses adalah data yang benar dan siap digunakan.

## 4. Kebutuhan `csrf_token` saat membuat form di Django
`csrf_token` di Django digunakan untuk melindungi form dari serangan Cross-Site Request Forgery (CSRF), yaitu serangan di mana penyerang mengirimkan permintaan berbahaya ke aplikasi dengan mengelabui pengguna yang sudah masuk. Jika tidak menambahkan `csrf_token`, penyerang bisa membuat pengguna yang tidak curiga mengirimkan data yang salah atau berbahaya tanpa mereka sadari. Hal itu dapat merusak data atau menyebabkan masalah keamanan. Jadi, intinya `csrf_token` memastikan bahwa setiap permintaan form benar-benar datang dari halaman yang sah dan bukan dari pihak luar.

## 5. Implementasi Checklist
Pada tugas 3 ini, hal baru yang saya pelajari adalah mengenai XML dan JSON yang merupakan motode data delivery.

Untuk mengimplementasikan hal tersebut, pertama-tama saya membuat berkas `base.html` sebagai template dasar untuk kerangka umum halaman web lainnya di dalam proyek. Halaman-halaman web lainnya (misalnya, `home.html`, `form.html`, dll) akan mengextend template `base.html`. Ini berarti mereka akan menggunakan struktur dasar dari base.html dan hanya menambahkan atau mengganti bagian-bagian tertentu sesuai kebutuhan mereka. Kemudian jadikan `base.html` menjadi templat utama pada `main.html`.

Selanjutnya, hal yang penting adalah membuat form. Struktur form dibuat pada berkas `forms.py` pada directory main kemudian mengimportnya di bagian `views.py` untuk membuat sebuah fungsi baru yang berguna untuk menghasilkan form yang dapat menambahkan data item secara otomatis ketika disubmit. Selain itu, berkas html yang baru berjudul `create_object_entry.html` juga dibuat untuk menampilkan data item dalam bentuk tabel. Berdasarkan tutorial 2, saya juga membuat xml, json, XML by ID, dan JSON by ID untuk mengembalikan data. Hal ini akan mengubah data hasil query dari database menjadi format yang bisa dipahami oleh client, seperti JSON atau XML. Di dalamnya berisi fungsi-fungsi yang mereturn HttpResponse untuk mengirimkan data ke client dengan JSON atau XML. Kemudian masing-masing views tersebut dibuatkan routing URL agar client dapat mengakses data dari server melalui URL tertentu dalam format yang diinginkan.

## Akses 4 URL dengan Postman
### xml
![ss_xml](https://github.com/user-attachments/assets/dbd8015d-ee79-478b-acf1-beaf1d7ef54c)

### json
![ss_json](https://github.com/user-attachments/assets/86fee7e1-edbe-4d04-a428-ff17cc5c7329)

### xml by ID
![ss_xml_id](https://github.com/user-attachments/assets/d6725ae7-e4e1-462e-8f9a-4d5c39e1f315)

### json by ID
![ss_xml_id](https://github.com/user-attachments/assets/623cc98f-3674-4ed0-ac01-4e2ea5bf27aa)


=========================================================================================================================================================================================================================================================================


# ------ T U G A S  4 -----  

## 1. perbedaan antara `HttpResponseRedirect()` dan `redirect()`
`HttpResponseRedirect()`digunakan untuk membuat respons HTTP dengan kode status 302 untuk menunjukkan bahwa halaman diminta untuk dialihkan atau redirect ke URL lain. Untunk menentukan URL atau path yang menjadi tujuan redirectnya harus manual. Biasanya digunakan untuk memanggil nama view. Sedangkan `redirect()` lebih fleksible karena bisa menerima URL langsung, nama view, dan objek model dengan methode `get_absolute_url()`. Oleh karena itu, redirect() ini disebut sebagai shortcut function yang disediakan oleh Django untuk menangani redirect(). Ia juga menggunakan `HttpResponseRedirect()` di belakang layarnya. Dengan begitu, redirect() lebih nyaman dan mudah dalam penulisan kode karena bisa langsung mengarahkan nama view tanpa harus menggunakan `reverse()` secara manual.

## 2. Cara kerja penghubungan model MoodEntry dengan User
User dijadikan variable yang merupakan foreign key pada MoodEntry (`user = models.ForeignKey(User, on_delete=models.CASCADE)`). Oleh karena itu, satu mood entry dimiliki oleh user yang uniq, tapi user bisa punya lebih dari satu MoodEntry sehingga user bisa input MoodEntry apapun dan berapapun tergantung keinginan. 

Pada kode `mood_entry = form.save(commit=False)` karena coomitnya bernilai false, form akan mwnunda penyimpanan input ke database. User yang sedang login menetapkan `request.user` sehingga data tersebut disimpan ke database dan informasinya dimasukkan ke field user itu sendiri dalam MoodEntry.

## 3. Perbedaan antara authentication dan authorization, Hal yang dilakukan saat pengguna login? Cara Django mengimplementasikan kedua konsep tersebut.
### Perbedaan antara authentication dan authorization
authentication adalah memastikan siapa pengguna tersebut dengan cara memverifikasi identitas. MIsalnya untuk login kita harus memasukan username dan kata sandi, aplikasi akan mengecek apak kedua hal tersebut sesuai. Sedangkan authorization memastikan apa yang diizinkan untuk dilakukan oleh pengguna berdasarkan izin aksesnya. Misalnya pada aplikasi ini, user boleh menambahkan Item berapapun.
### Hal yang dilakukan saat pengguna login?
Saat login, pengguna bisa menambahkan Item apa saja dengan melengkapi data-data item yang diperlukan. Pengguna boleh menambahkan berapa saja tanpa batasan sesuai keperluan. 
### Cara Django mengimplementasikan kedua konsep tersebut.
1) Django mengimplementasikan `authentication` dengan menyediakan formulir bawaan `UserCreationForm` yang pada tutorial kemarin disimpan pada `views.py` dan juga menyediakan fungsi `AuthenticationForm`. Pada bagian `AuthenticationForm(data=request.POST)` berfungsi untuk memvalidasi apakah data yang dimasukan saat login benar atau tidak. Jika benar, maka user akan berhasil masuk dan memiliki hak akses pada aplikasi tergantung akunnya.
2) Django juga mengimplementasikan authorization dengan cara menyediakan `@login_required` untuk membatasi hak akses ke halaman tertentu. Contohnya pada aplikasi ini kita menyimpan `@login_required(login_url='/login')` di atas show_main. Jadi pengguna harus login dulu sebelum memiliki akses untuk menambahkan data-data pada aplikasi.

## 4. Cara Django mengingat pengguna yang sudah login dan kegunaan lain cookie
### Cara Django mengingat pengguna yang sudah login
Django mengingat pengguna yang telah login dengan melakukan session framework yang sessionnya disimpan ke database dan mereferensikannya dengan cookies. Ketika pengguna berhasil login, Dango akan membuat session ID yang uniq untuk setiap pengguna lalu mengirimkan session ID tersebut sebagai cookie ke browser pengguna setelah menyimpannya di server. Setiap kali user request, session ID dikirim juga dengan request tersebut hingga server mengenali user dan memberikan akses sesuai status login.
### Kegunaan lain cookie
Cookies berguna untuk menyimpan preferensi pengguna seperti pilihan bahasa, tema, atau pengaturan tampilan lainnya. Selain itu cookies juga digunakan oleh pihak ketiga untuk melacak aktivitas pengguna di berbagai situs web. Cookies juga memungkinkan pengguna untuk login ke beberapa aplikasi dalam satu sesi tanpa harus login berulang kali.
Namun, tidak semua cookies aman. Jika cookie dikirim melalui koneksi HTTP biasa atau tanpa pengamanan tambahan, cookie tersebut rentan terhadap serangan penyadapan (man-in-the-middle) atau pencurian melalui serangan XSS.

## 5. Cara mengimplementasikan checklist di atas secara step-by-step
Pada tugas 4 ini, hal baru yang saya pelajari adalah mengenai pembuatan form untuk user yang dihubungkan dengan model dengan menjadikan user sebagai foreign key sehingga user dapat membuat beberapa input item. 

Pertama-tama, saya membuat fungsi registrasi yang memungkinkan user untuk membuat akun baru. Dalam `views.py`, saya menggunakan `UserCreationForm` dari Django untuk memvalidasi dan menyimpan data pengguna. Setelah itu, saya membuat template `register.html` yang akan menampilkan formulir pendaftaran yang kemudian menambahkan URL untuk mengakses halaman registrasi. 

Saya mengimplementasikan login menggunakan `AuthenticationForm` di Django yang akan melakukan autentikasi pengguna berdasarkan username dan password yang dimasukkan. Jika autentikasi berhasil, pengguna akan diarahkan ke halaman utama aplikasi. Saya juga membuat `login.html` untuk menampilkan form login dan juga menambhakn URL login. Kemudian, saya membuat fungsi logout yang menggunakan `logout` dari Django untuk mengakhiri sesi pengguna untuk kembali ke halaman login.

Untuk membuat dua akun pengguna, saya menggunakan form registrasi dan kemudian menambahkan tiga data dummy untuk setiap akun di model item yang telah dibuat sebelumnya. Pada tahap ini, saya juga menghubungkan model Product dengan User dengan menambahkan field `user` sebagai `ForeignKey` dalam model Product. Saat menyimpan data produk baru, saya memastikan bahwa pengguna yang sedang login terkait dengan produk yang dibuat.Saya menampilkan nama pengguna yang sedang login di aplikasi (Halo {{nama}}), termasuk username dan waktu terakhir login yang disimpan dalam cookie. Fungsi login saya modifikasi agar menyimpan informasi login terakhir ke cookie, dan informasi ini ditampilkan di halaman utama menggunakan template HTML. Dengan demikian, pengguna dapat melihat kapan terakhir loginnya.


=========================================================================================================================================================================================================================================================================


# ------ T U G A S  5 -----  

## 1. Urutan prioritas pengambilan CSS selector
Ketika kita menggunakan CSS untuk styling halaman web, terkadang satu elemen HTML memiliki lebih dari satu style yang diterapkan dari beberapa selector yang berbeda. Dalam kasus seperti ini, browser akan menentukan prioritas berdasarkan aturan specificity. Specificity ini menentukan mana CSS yang akan diutamakan.
1. Selector Berdasarkan Nama Elemen (Element Selector)
Selector ini adalah yang paling dasar dan memiliki prioritas paling rendah. Element selector memilih elemen HTML berdasarkan tag-nya, seperti `<p>`, `<div>`, atau `<h1>`. 
2. Selector Berdasarkan Class (Class Selector)
Selector ini lebih spesifik daripada element selector. Class selector menggunakan atribut class dalam elemen HTML untuk menerapkan style. Sebagai contoh, `.button { background-color: green; }` akan mengubah warna latar belakang elemen yang memiliki class button. 
3. Selector Berdasarkan Atribut dan Pseudo-class
Selector berdasarkan atribut memilih elemen HTML yang memiliki atribut tertentu, seperti `[type="text"]`. Pseudo-class, seperti `:hover` atau `:focus`, digunakan untuk memilih elemen dalam kondisi tertentu. Misalnya, `a:hover { color: red; }` akan mengubah warna tautan saat di-hover menjadi merah. Selector ini memiliki prioritas yang sama dengan class selector.
4. Selector Berdasarkan ID (ID Selector)
Selector ID sangat spesifik dan memiliki prioritas yang lebih tinggi dibandingkan class dan element selector. ID adalah unik untuk setiap elemen di halaman, sehingga style yang diterapkan melalui ID akan diutamakan. Misalnya, `#header { background-color: black; }` akan mengubah warna latar belakang elemen dengan ID header menjadi hitam, meskipun ada class atau element selector lain yang memberikan aturan berbeda.
5. Inline Styles
Inline styles adalah style yang ditulis langsung di dalam atribut style elemen HTML. Misalnya, `<h1 style="color: red;">Hello</h1>`. Inline styles memiliki prioritas yang lebih tinggi dibandingkan semua selector CSS lainnya yang ditulis di file eksternal atau internal. Ini berarti jika ada style yang diterapkan langsung pada elemen melalui inline styles, style tersebut akan mengabaikan selector lain, kecuali ada aturan `!important`.

## 2. Alasan responsive design menjadi konsep yang penting dalam pengembangan aplikasi web
Responsive design adalah pendekatan dalam pengembangan aplikasi web yang bertujuan untuk membuat tampilan situs web dapat beradaptasi dengan baik di berbagai ukuran layar dan perangkat, seperti smartphone, tablet, dan desktop. esponsive design memastikan bahwa pengguna memiliki pengalaman yang konsisten dan optimal, terlepas dari perangkat yang mereka gunakan. Selain itu, Responsive design membuat aplikasi web dapat diakses dengan mudah oleh semua orang, termasuk mereka yang memiliki keterbatasan fisik atau keterampilan teknologi.
1. Aplikasi yang sudah menerapkan responsive design: Doramiaw (hehe)
Saya membuat beberapa halaman dari aplikasi ini dengan responsive design. Contohnya halaman yang memuat navbar, saya membuat navbar tersebut menjadi responsive. Saat layar dikecilkan, menu yang semula ditambilkan di tengah-atar halaman, menjadi ditampilkan saat hamburger diklik.
2. Aplikasi yang belum menerapkan responsive design: Beberapa Situs Berita Tua
Beberapa situs berita yang lebih tua masih memiliki desain yang tidak responsif, sehingga tampilan mereka tidak optimal di perangkat mobile. Pengguna mungkin mengalami kesulitan saat mengakses konten, karena harus menggulir secara horizontal atau memperbesar untuk membaca artikel.

## 3. Perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
1. Margin
Margin adalah ruang kosong di luar batas elemen. Ini adalah area antara elemen dan elemen lain di sekitarnya. Margin tidak memiliki warna dan bersifat transparan.
contoh implementasi: 
.element {
    margin: 10px 20px; /* 10px atas dan bawah, 20px kanan dan kiri */
}
2. Border
Border adalah garis yang mengelilingi elemen. Border dapat memiliki ketebalan, warna, dan jenis garis yang berbeda (seperti solid, dashed, atau dotted).
contoh implementasi: 
.element {
    border: 2px solid black; /* Ketebalan 2px, jenis solid, dan warna hitam */
}
3. Padding
Padding adalah ruang di dalam batas elemen, antara konten elemen (seperti teks atau gambar) dan batas itu sendiri. Padding memiliki warna latar belakang yang sama dengan elemen.
contoh implementasi: 
.element (class element contohny) {
    padding: 15px; /* Mengatur padding 15px di semua sisi */
}
> I N T I N Y A: Margin adalah ruang di luar elemen, digunakan untuk mengatur jarak antar elemen. Border adalah garis yang mengelilingi elemen, memberikan batas visual. Padding adalah ruang di dalam elemen, memberikan jarak antara konten dan batas.

## 4. Konsep flex box dan grid layout beserta kegunaannya!
1. Flex Box
Flexbox, atau Flexible Box Layout, adalah metode tata letak CSS yang dirancang untuk mengatur elemen dalam satu dimensi, baik secara horizontal maupun vertikal. Flexbox memudahkan pengaturan spasi di antara elemen dan mengontrol ukuran elemen agar dapat beradaptasi dengan berbagai ukuran layar.
>Kegunaan: Menyusun elemen dalam satu baris atau kolom, Mengatur spasi dan perataan elemen, Menangani ukuran elemen yang responsif.
2. Grid Layout
Grid Layout adalah metode tata letak CSS yang memungkinkan pengembang untuk mengatur elemen dalam dua dimensi, baik secara horizontal maupun vertikal. Dengan Grid, elemen dapat disusun dalam baris dan kolom, menciptakan struktur yang lebih kompleks dibandingkan Flexbox.
>Kegunaan: Membuat desain yang kompleks seperti tata letak grid untuk gambar, artikel, atau kartu produk, Memberikan kontrol yang lebih besar atas penempatan elemen di halaman, Mendukung desain responsif dngan mengatur ukuran kolom dan baris menggunakan fraksi atau persentase, grid dapat beradaptasi dengan baik pada berbagai ukuran layar.

## 5. Cara mengimplementasikan checklist di atas secara step-by-step
Untuk mengimplementasikan fungsi hapus dan edit produk, langkah pertama yang dibuat adalah membuat view function pada `views.py` untuk menangani proses penghapusan dan pengeditan produk. dan melakukan routing pada `urls.py` untuk mengarahkan permintaan edit dan delete ke view yang tepat. Di dalam template HTML yang menampilkan daftar produk, tambahkan dua tombol di setiap card produk: satu untuk "Edit" dan satu untuk "Delete". 

Untuk mengkustomisasi halaman login, register, dan tambah produk, saya membuat halaman-halaman tersebut secara terpisah dan membuat mereka memiliki tampilan yang menarik dengan CSS. Saya tidak menggunakan CSS framwork karena kemampuan saya dalam hal tersebut masih terbatas untuk menyelesaikan tugas yang deadline-nya tinggal sebentar. Jadi saya memutuskan untuk memakai kemampuan yang saya miliki dengan menggunakan CSS ini.

Untuk tampilan pesan saat produk belum diinput, pada fungsi `views.py` saya mengecek terlebih dahulu apakah memang tisak ada produk. Jika tidak ada, maka saya menampilkan pesan dan gambar doraemon sedih pada halaman. 

Untuk implementasi navigation Bar yang responsif, saya membuat  struktur dasar navbar yang berisi daftar menu, dan tombol untuk login/logout kemudian membuat tampilannya menjadi menarik di file css. Agar responsif di mobile, saya menggunakan media query untuk mengubah layout saat tampilan di layar lebih kecil (di bawah 950px). Kemudian menambahkan JavaScript untuk mengaktifkan/menonaktifkan tampilan menu ketika tombol hamburger diklik.
