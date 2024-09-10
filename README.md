1. cara saya mengimplementasikan semua checklist yang ditentukan
Untuk mulai mengerjakan tugas ini, saya membuat repository di GitHub dengan nama e-commerce saya yaitu Doramiaw. Setelah itu, saya mengcloning repository tersebut pada laptop saya agar bisa dikerjakan secra lokal. Saat ada beberapa perubahan, saya meng-add, commit, push pada github. Repositori yang saya buat dibranching pada branch Main. Saya mengaktifkan environment pada cmd, lalu mulai membuat proyek django dengan nama "Doramiaw". Hal pertama yang saya lakukan adalah membuat file requirements.txt yang berisi beberapa dependencies lalu menginstall dependencies tersebut. Tidak lupa pula menambahkan host pada settings.py agar aplikasi web dapat diakses. 

Selanjutnya, saya membuat berkas .gitignore agar beberapa berkas direktori yang tidak perlu dilacak dapat diabaikan oleh Git (tidak masuk ke dalam versi kontrol Git). 

Saya membuat aplikasi main di dalam projek Doramiaw. Pada settings.py saya menambahkan aplikasi tersebut pada variable INSTALLED_APPS untuk mendaftarkan aplikasi yang dibuat pada projek. Kemudian di dalam folder main, saya membuat folder template yang berisi html. Saya mengisii html tersebut dengan kode-kode berdasakan design e-commerce yang akan saya buat. Setelah selesai, saya mengubah isi file model.py dengan data-data produk pada ecommerce saya lalu melakukan makemigrations dan migrasi untuk mengaplikasikan perubahan yang saya buat dalam model. Template yang saya buat tersebut dihubungkan juga dengan view. Pada urls.py dalam direktori main saya mengatur rute URL yang terkait dengan aplikasi main sedangkan pada urls.py di proyek, saya mengimpor rute URL dari berkas urls.py aplikasi main. 

Pada langkah terakhir setelah semua langkah diatas diaplikasikan, saya mulai push direktory tersebut ke pws. Langkah ini saya lakukan terakhir karena pada saat pengerjaan tugas ini dilaksanakan, pws sedang bermasalah dan baru bisa digunakan ketika tugas saya selesai. 



2. Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![bagan django](bagan-django.png)


3. Fungsi git dalam pengembangan perangkat lunak!
Dalam membuat kode untuk suatu program, tentunya tidak akan bisa hanya dalam sekali duduk apalagi jika program yang dibuat sangat besar. Apalagi jika banyak revisi yang harus dilakukan. Dengan menggunakan git, kita dapat menyimpan versi yang berbeda dari kode sumber. Selain itu, git juga berfungsi untuk kolaborasi tim yang bekerja pada projek yang sama tanpa saling mengganggu satu sama lain.


4. Framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak
Django cocok untuk pemula karena memiliki fitur yang lengkap seperti interakti ke database dan sistem routing, struktur yang jelas anatara MVT (model, views, template), dan dokumentasi yang sangat baik. 


5. Alasan model pada Django disebut sebagai ORM
Model disebut ORM karena berfungsi sebagai penghubung antara database dan kode objek. Jadi programer bisa membuat, membaca, memperbarui, dan hapus menggunakan objek Python tanpa harus menulis query SQL secara langsung. Setiap model di Django adalah representasi dari tabel di database, dan atribut-atribut di dalam model merepresentasikan kolom-kolom dalam tabel tersebut.
