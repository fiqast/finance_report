from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Koneksi database
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',  # Sesuaikan dengan username MySQL Anda
        password='',  # Sesuaikan dengan password MySQL Anda
        database='keuangan_mahasiswa'  # Nama database
    )
    return conn

@app.route('/')
def index():
    # Koneksi ke database
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Ambil kategori dari database
    cursor.execute('SELECT * FROM kategori_pengeluaran')
    kategori_pengeluaran = cursor.fetchall()

    # Ambil transaksi beserta kategori yang terkait
    cursor.execute(''' 
        SELECT transaksi.id, transaksi.tanggal, transaksi.tipe, transaksi.jumlah, transaksi.keterangan, 
               GROUP_CONCAT(kategori_transaksi.kategori) AS kategori
        FROM transaksi
        LEFT JOIN kategori_transaksi ON transaksi.id = kategori_transaksi.transaksi_id
        GROUP BY transaksi.id
        ORDER BY transaksi.tanggal DESC
    ''')
    transaksi = cursor.fetchall()

    # Hitung total pemasukan dan pengeluaran
    cursor.execute('''SELECT SUM(jumlah) FROM transaksi WHERE tipe = 'Pemasukan' ''')
    total_pemasukan = cursor.fetchone()['SUM(jumlah)'] or 0

    cursor.execute('''SELECT SUM(jumlah) FROM transaksi WHERE tipe = 'Pengeluaran' ''')
    total_pengeluaran = cursor.fetchone()['SUM(jumlah)'] or 0

    saldo = total_pemasukan - total_pengeluaran

    conn.close()

    return render_template('index.html', 
                           kategori_pengeluaran=kategori_pengeluaran, 
                           transaksi=transaksi, 
                           saldo=saldo)


@app.route('/tambah_transaksi', methods=['POST'])
def tambah_transaksi():
    tanggal = request.form['tanggal']
    kategori = request.form.getlist('kategori')  # Mengambil beberapa kategori yang dipilih
    kategori_kustom = request.form['kategori_kustom']
    tipe = request.form['tipe']
    jumlah = request.form['jumlah']
    keterangan = request.form['keterangan']

    # Menambahkan kategori kustom jika ada
    if kategori_kustom:
        kategori.append(kategori_kustom)

    # Simpan transaksi ke database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Menambahkan transaksi ke database
    cursor.execute(''' 
        INSERT INTO transaksi (tanggal, tipe, jumlah, keterangan)
        VALUES (%s, %s, %s, %s)
    ''', (tanggal, tipe, jumlah, keterangan))
    transaksi_id = cursor.lastrowid

    # Menyimpan kategori yang dipilih (termasuk kategori kustom)
    for kat in kategori:
        cursor.execute(''' 
            INSERT INTO kategori_transaksi (transaksi_id, kategori)
            VALUES (%s, %s)
        ''', (transaksi_id, kat))

    conn.commit()
    conn.close()

    return redirect(url_for('index'))

@app.route('/laporan')
def laporan():
    # Koneksi ke database
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Mengambil data laporan bulanan
    cursor.execute('''
        SELECT DATE_FORMAT(tanggal, '%M') AS bulan, 
               tipe, 
               SUM(jumlah) AS total
        FROM transaksi
        GROUP BY bulan, tipe
        ORDER BY MONTH(tanggal)
    ''')
    laporan_data = cursor.fetchall()
    conn.close()

    # Strukturkan data menjadi format {bulan: {tipe: total}}
    laporan_terstruktur = {}
    for row in laporan_data:
        bulan = row['bulan']
        tipe = row['tipe']
        total = row['total']

        if bulan not in laporan_terstruktur:
            laporan_terstruktur[bulan] = {'Pemasukan': 0, 'Pengeluaran': 0}
        laporan_terstruktur[bulan][tipe] = total

    return render_template('laporan.html', laporan=laporan_terstruktur)


if __name__ == '__main__':
    app.run(debug=True)
