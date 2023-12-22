import unittest
import sqlite3
import tkinter as tk
from tkinter import ttk
import customtkinter  # Assuming customtkinter is your custom module

class TestPembeliFunctions(unittest.TestCase):
    def setUp(self):
        # Connect to an in-memory SQLite database for testing
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.create_table()

        # Create a Tkinter root window for testing
        self.root = tk.Tk()
        self.content_frame = tk.Frame(self.root)
        self.treeview = ttk.Treeview(self.content_frame, columns=("ID", "Nama", "No_HP", "Alamat", "Kota"),
                                     show="headings", height=25)
        self.treeview.grid(row=5, columnspan=3, padx=5, pady=30)

        # Initialize entry widgets for testing
        self.entry_nama = customtkinter.CTkEntry(self.content_frame, width=200)
        self.entry_no_hp = customtkinter.CTkEntry(self.content_frame, width=200)
        self.entry_alamat = customtkinter.CTkEntry(self.content_frame, width=200)
        self.entry_kota = customtkinter.CTkEntry(self.content_frame, width=200)

    def tearDown(self):
        # Close the database connection and destroy the Tkinter root window
        self.conn.close()
        self.root.destroy()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE Pembeli (
                ID_Pembeli INTEGER PRIMARY KEY AUTOINCREMENT,
                Nama TEXT,
                No_HP TEXT,
                Alamat TEXT,
                Kota TEXT
            )
        ''')
        self.conn.commit()

    def add_pembeli(self):
        # Fetch values from the entry fields
        nama = self.entry_nama.get()
        no_hp = self.entry_no_hp.get()
        alamat = self.entry_alamat.get()
        kota = self.entry_kota.get()

        # Insert new "Pembeli" record into the database
        self.cursor.execute("INSERT INTO Pembeli (Nama, No_HP, Alamat, Kota) VALUES (?, ?, ?, ?)",
                            (nama, no_hp, alamat, kota))
        self.conn.commit()


    def test_add_pembeli(self):
        # Test adding a new Pembeli record
        self.add_pembeli()

        # Check if the record was added to the database
        self.cursor.execute("SELECT * FROM Pembeli")
        rows = self.cursor.fetchall()
        self.assertEqual(len(rows), 1)

if __name__ == '__main__':
    unittest.main()
