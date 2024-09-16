Berikut adalah perbaikan penulisan untuk file `README.md` yang lebih terstruktur dan rapi:

---

# Doramiaw E-commerce

### Nama: Irma Nia Alwijah  
### NPM: 2306226864  
### Kelas: PBP B  

[Link PWS](http://irma-nia-doramiaw.pbp.cs.ui.ac.id)

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

### Penjelasan

- **urls.py**: Berfungsi untuk memetakan URL yang di-request oleh pengguna ke views yang sesuai.
- **views.py**: Menangani logika aplikasi dan mengambil/memproses data dari models atau permintaan lainnya.
- **models.py**: Mengelola data dan struktur database, serta menghubungkan dengan ORM (Object-Relational Mapping) Django.
- **HTML template**: Merupakan representasi dari antarmuka pengguna yang dikirimkan sebagai respons.

## 3. Fungsi Git dalam Pengembangan Perangkat Lunak

Git berfungsi sebagai sistem kontrol versi yang memungkinkan kita menyimpan, mengelola, dan melacak perubahan dalam kode. Hal ini sangat membantu saat melakukan revisi berkala dan bekerja dalam tim, karena memungkinkan kolaborasi tanpa saling mengganggu satu sama lain.

## 4. Alasan Django Dipilih untuk Belajar Pengembangan Perangkat Lunak

Django cocok untuk pemula karena menyediakan banyak fitur bawaan seperti interaksi dengan database, sistem routing, dan keamanan. Django juga memiliki struktur yang jelas dengan menggunakan pola Model-View-Template (MVT), serta dokumentasi yang lengkap dan mudah dipahami.

## 5. Mengapa Model di Django Disebut sebagai ORM

Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena berfungsi sebagai penghubung antara kode Python dan database. Melalui ORM, kita bisa membuat, membaca, memperbarui, dan menghapus data dari database tanpa menulis query SQL secara langsung. Setiap model merepresentasikan tabel di database, dan atribut di dalamnya merepresentasikan kolom-kolom tabel tersebut.
