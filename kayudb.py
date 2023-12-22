import sqlite3

# Connect to the SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect('kayu.sqlite')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Define the "Supplier" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Supplier (
        ID_Supplier INTEGER PRIMARY KEY AUTOINCREMENT,
        Nama TEXT,
        No_HP INTEGER,
        Alamat TEXT,
        Bukti_Kepemilikan TEXT,
        No_Bukti_Kepemilikan INTEGER,
        NIK_Pengirim INTEGER
    )
''')

# Define the "Pembeli" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pembeli (
        ID_Pembeli INTEGER PRIMARY KEY AUTOINCREMENT,
        Nama TEXT,
        No_HP REAL,
        Alamat TEXT,
        Kota Text
    )
''')

# Define the "Akun" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Akun (
        ID_Akun TEXT PRIMARY KEY,
        Nama TEXT,
        Kategori TEXT
    )
''')

# Define the "Log Kayu" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Log_Kayu (
        ID_Log_Kayu INTEGER PRIMARY KEY AUTOINCREMENT,
        Nama TEXT,
        Panjang REAL
    )
''')

# Define the "Hasil Produksi" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Hasil_Produksi (
        ID_Hasil_Produksi INTEGER PRIMARY KEY AUTOINCREMENT,
        Nama TEXT,
        Jenis TEXT
    )
''')

# Define the "Aset Tetap" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Aset_Tetap (
        ID_Aset_Tetap INTEGER PRIMARY KEY AUTOINCREMENT,
        ID_Akun TEXT,
        Tanggal_Beli DATE,
        Keterangan TEXT,
        Harga_Beli REAL,
        Jumlah INTEGER,
        Umur_Ekonomis INTEGER,
        Kondisi TEXT,
        Dari_Akun TEXT,
        FOREIGN KEY (ID_Akun) REFERENCES Akun (ID_Akun),
        FOREIGN KEY (ID_Akun) REFERENCES Akun (Dari_Akun)
    )
''')

# Define the "Biaya" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Biaya (
        ID_Biaya INTEGER PRIMARY KEY AUTOINCREMENT,
        ID_Akun TEXT,
        Penerima TEXT,
        Tanggal_Terima DATE,
        Keterangan TEXT,
        Pembayaran REAL,
        Dari_Akun TEXT,
        FOREIGN KEY (ID_Akun) REFERENCES Akun (ID_Akun),
        FOREIGN KEY (ID_Akun) REFERENCES Akun (Dari_Akun)
    )
''')

# Define the "Pembelian" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pembelian (
        ID_Pembelian INTEGER PRIMARY KEY AUTOINCREMENT,
        ID_Supplier INTEGER,
        ID_Akun TEXT,
        Tanggal_Surat_Jalan DATE,
        Tanggal_Nota DATE,
        Bea_Supplier REAL,
        Termin TEXT,
        Pembayaran REAL,
        FOREIGN KEY (ID_Supplier) REFERENCES Supplier (ID_Supplier),
        FOREIGN KEY (ID_Akun) REFERENCES Akun (ID_Akun)
    )
''')

# Define the "Detail Beli" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Detail_Beli (
        ID_Detail_Beli INTEGER PRIMARY KEY AUTOINCREMENT,
        ID_Pembelian INTEGER,
        ID_Log_Kayu INTEGER,
        Diameter REAL,
        Jumlah INTEGER,
        Pembulatan INTEGER,
        Harga_Beli REAL,
        FOREIGN KEY (ID_Pembelian) REFERENCES Pembelian (ID_Pembelian),
        FOREIGN KEY (ID_Log_Kayu) REFERENCES Log_Kayu (ID_Log_Kayu)
    )
''')

# Define the "Utang" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Utang (
        ID_Utang INTEGER PRIMARY KEY AUTOINCREMENT,
        ID_Pembelian INTEGER,
        ID_Akun TEXT,
        Tanggal DATE,
        Pembayaran REAL,
        FOREIGN KEY (ID_Pembelian) REFERENCES Pembelian (ID_Pembelian),
        FOREIGN KEY (ID_Akun) REFERENCES Akun (ID_Akun)
    )
''')

# Define the "Produksi" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Produksi (
        ID_Produksi INTEGER PRIMARY KEY AUTOINCREMENT,
        ID_Pembelian INTEGER,
        Tanggal_Produksi DATE,
        FOREIGN KEY (ID_Pembelian) REFERENCES Pembelian (ID_Pembelian)
    )
''')

# Define the "Detail Produksi" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Detail_Produksi (
        ID_Detail_Produksi INTEGER PRIMARY KEY AUTOINCREMENT,
        ID_Produksi INTEGER,
        ID_Hasil_Produksi INTEGER,
        Tebal REAL,
        Ukuran REAL,
        Jumlah INTEGER,
        FOREIGN KEY (ID_Produksi) REFERENCES Produksi (ID_Produksi),
        FOREIGN KEY (ID_Hasil_Produksi) REFERENCES Hasil_Produksi (ID_Hasil_Produksi)
    )
''')

# Define the "Penjualan" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Penjualan (
        ID_Penjualan INTEGER PRIMARY KEY AUTOINCREMENT,
        ID_Pembeli INTEGER,
        ID_Akun TEXT,
        Tanggal_Sales_Order DATE,
        Nomor_Sales_Order TEXT,
        Tanggal_Surat_Jalan DATE,
        Tanggal_Faktur DATE,
        Termin TEXT,
        Pembayaran REAL,
        Alat_Angkutan TEXT,
        Identitas_Kendaraan TEXT,
        PPN_Keluaran TEXT,
        FOREIGN KEY (ID_Pembeli) REFERENCES Pembeli (ID_Pembeli),
        FOREIGN KEY (ID_Akun) REFERENCES Akun (ID_Akun)
    )
''')

# Define the "Detail Jual" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Detail_Jual (
        ID_Detail_Jual INTEGER PRIMARY KEY AUTOINCREMENT,
        ID_Penjualan INTEGER,
        ID_Hasil_Produksi INTEGER,
        Tebal REAL,
        Ukuran REAL,
        Jumlah INTEGER,
        Keterangan TEXT,
        Harga_Jual REAL,
        FOREIGN KEY (ID_Penjualan) REFERENCES Penjualan (ID_Penjualan),
        FOREIGN KEY (ID_Hasil_Produksi) REFERENCES Hasil_Produksi (ID_Hasil_Produksi)
    )
''')

# Define the "Piutang" table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Piutang (
        ID_Piutang INTEGER PRIMARY KEY AUTOINCREMENT,
        ID_Penjualan INTEGER,
        ID_Akun TEXT,
        Tanggal DATE,
        Pembayaran REAL,
        FOREIGN KEY (ID_Penjualan) REFERENCES Penjualan (ID_Penjualan),
        FOREIGN KEY (ID_Akun) REFERENCES Akun (ID_Akun)
    )
''')

# Commit the changes and close the database connection
conn.commit()
conn.close()