
# Doramiaw E-commerce

### Nama: Irma Nia Alwijah  
### NPM: 2306226864  
### Kelas: PBP B  

[Link PWS](http://irma-nia-doramiaw.pbp.cs.ui.ac.id)

## ------ T U G A S  2 -----  

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


### ------ T U G A S  3 -----  

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


### ------ T U G A S  4 -----  

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