import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host='103.163.138.101',
    port='3306',
    user='orionedu_addis',
    password='Rheza191421',
    database='orionedu_kayu'
)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Define the "Supplier" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Supplier (
        ID_Supplier INT AUTO_INCREMENT PRIMARY KEY,
        Nama VARCHAR(255),
        No_HP VARCHAR(255),
        Alamat TEXT,
        Bukti_Kepemilikan TEXT,
        No_Bukti_Kepemilikan INT,
        NIK_Pengirim INT
    )
''')

# Define the "Pembeli" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pembeli (
        ID_Pembeli INT AUTO_INCREMENT PRIMARY KEY,
        Nama VARCHAR(255),
        No_HP VARCHAR(255),
        Alamat TEXT,
        Kota VARCHAR(255)
    )
''')

# Define the "Akun" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Akun (
        ID_Akun VARCHAR(255) PRIMARY KEY,
        Nama VARCHAR(255),
        Kategori VARCHAR(255)
    )
''')

# Define the "Log Kayu" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Log_Kayu (
        ID_Log_Kayu INT AUTO_INCREMENT PRIMARY KEY,
        Nama VARCHAR(255),
        Panjang FLOAT
    )
''')

# Define the "Hasil Produksi" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Hasil_Produksi (
        ID_Hasil_Produksi INT AUTO_INCREMENT PRIMARY KEY,
        Nama VARCHAR(255),
        Jenis VARCHAR(255)
    )
''')

# Define the "Aset Tetap" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Aset_Tetap (
        ID_Aset_Tetap INT AUTO_INCREMENT PRIMARY KEY,
        ID_Akun VARCHAR(255),
        Tanggal_Beli DATE,
        Keterangan TEXT,
        Harga_Beli FLOAT,
        Jumlah INT,
        Umur_Ekonomis INT,
        Kondisi TEXT,
        Dari_Akun VARCHAR(255),
        FOREIGN KEY (ID_Akun) REFERENCES Akun (ID_Akun),
        FOREIGN KEY (Dari_Akun) REFERENCES Akun (ID_Akun)
    )
''')

# Define the "Biaya" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Biaya (
        ID_Biaya INT AUTO_INCREMENT PRIMARY KEY,
        ID_Akun VARCHAR(255),
        Penerima VARCHAR(255),
        Tanggal_Terima DATE,
        Keterangan TEXT,
        Pembayaran FLOAT,
        Dari_Akun VARCHAR(255),
        FOREIGN KEY (ID_Akun) REFERENCES Akun (ID_Akun),
        FOREIGN KEY (Dari_Akun) REFERENCES Akun (ID_Akun)
    )
''')

# Define the "Pembelian" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pembelian (
        ID_Pembelian INT AUTO_INCREMENT PRIMARY KEY,
        ID_Supplier INT,
        ID_Akun VARCHAR(255),
        Tanggal_Surat_Jalan DATE,
        Tanggal_Nota DATE,
        Bea_Supplier FLOAT,
        Termin TEXT,
        Pembayaran FLOAT,
        FOREIGN KEY (ID_Supplier) REFERENCES Supplier (ID_Supplier),
        FOREIGN KEY (ID_Akun) REFERENCES Akun (ID_Akun)
    )
''')

# Define the "Detail Beli" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Detail_Beli (
        ID_Detail_Beli INT AUTO_INCREMENT PRIMARY KEY,
        ID_Pembelian INT,
        ID_Log_Kayu INT,
        Diameter FLOAT,
        Jumlah INT,
        Pembulatan INT,
        Harga_Beli FLOAT,
        FOREIGN KEY (ID_Pembelian) REFERENCES Pembelian (ID_Pembelian),
        FOREIGN KEY (ID_Log_Kayu) REFERENCES Log_Kayu (ID_Log_Kayu)
    )
''')

# Define the "Utang" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Utang (
        ID_Utang INT AUTO_INCREMENT PRIMARY KEY,
        ID_Pembelian INT,
        ID_Akun VARCHAR(255),
        Tanggal DATE,
        Pembayaran FLOAT,
        FOREIGN KEY (ID_Pembelian) REFERENCES Pembelian (ID_Pembelian),
        FOREIGN KEY (ID_Akun) REFERENCES Akun (ID_Akun)
    )
''')

# Define the "Produksi" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Produksi (
        ID_Produksi INT AUTO_INCREMENT PRIMARY KEY,
        ID_Pembelian INT,
        Tanggal_Produksi DATE,
        FOREIGN KEY (ID_Pembelian) REFERENCES Pembelian (ID_Pembelian)
    )
''')

# Define the "Detail Produksi" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Detail_Produksi (
        ID_Detail_Produksi INT AUTO_INCREMENT PRIMARY KEY,
        ID_Produksi INT,
        ID_Hasil_Produksi INT,
        Tebal FLOAT,
        Ukuran FLOAT,
        Jumlah INT,
        FOREIGN KEY (ID_Produksi) REFERENCES Produksi (ID_Produksi),
        FOREIGN KEY (ID_Hasil_Produksi) REFERENCES Hasil_Produksi (ID_Hasil_Produksi)
    )
''')

# Define the "Penjualan" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Penjualan (
        ID_Penjualan INT AUTO_INCREMENT PRIMARY KEY,
        ID_Pembeli INT,
        ID_Akun VARCHAR(255),
        Tanggal_Sales_Order DATE,
        Nomor_Sales_Order VARCHAR(255),
        Tanggal_Surat_Jalan DATE,
        Tanggal_Faktur DATE,
        Termin TEXT,
        Pembayaran FLOAT,
        Alat_Angkutan VARCHAR(255),
        Identitas_Kendaraan VARCHAR(255),
        PPN_Keluaran VARCHAR(255),
        FOREIGN KEY (ID_Pembeli) REFERENCES Pembeli (ID_Pembeli),
        FOREIGN KEY (ID_Akun) REFERENCES Akun (ID_Akun)
    )
''')

# Define the "Detail Jual" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Detail_Jual (
        ID_Detail_Jual INT AUTO_INCREMENT PRIMARY KEY,
        ID_Penjualan INT,
        ID_Hasil_Produksi INT,
        Tebal FLOAT,
        Ukuran FLOAT,
        Jumlah INT,
        Keterangan TEXT,
        Harga_Jual FLOAT,
        FOREIGN KEY (ID_Penjualan) REFERENCES Penjualan (ID_Penjualan),
        FOREIGN KEY (ID_Hasil_Produksi) REFERENCES Hasil_Produksi (ID_Hasil_Produksi)
    )
''')

# Define the "Piutang" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Piutang (
        ID_Piutang INT AUTO_INCREMENT PRIMARY KEY,
        ID_Penjualan INT,
        ID_Akun VARCHAR(255),
        Tanggal DATE,
        Pembayaran FLOAT,
        FOREIGN KEY (ID_Penjualan) REFERENCES Penjualan (ID_Penjualan),
        FOREIGN KEY (ID_Akun) REFERENCES Akun (ID_Akun)
    )
''')

# Commit the changes and close the database connection
conn.commit()
conn.close()
