Berikut adalah perbaikan penulisan untuk file `README.md` yang lebih terstruktur dan rapi:

---

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
### json
### xml by ID
### json by ID
