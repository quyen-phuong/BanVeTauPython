from tkinter.ttk import *
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import mysql.connector

def show_ThongKe(frame_noidung):
    for widget in frame_noidung.winfo_children():
        widget.destroy()

    def ketnoi():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="quanlybanve"
        )

    def get_total_customers():
        conn = ketnoi()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM khachhang")
        total_customers = cursor.fetchone()[0]
        conn.close()
        return total_customers

    def get_total_trains():
        conn = ketnoi()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM tau")
        total_trains = cursor.fetchone()[0]
        conn.close()
        return total_trains

    def get_total_seats_per_train():
        conn = ketnoi()
        cursor = conn.cursor()
        cursor.execute("SELECT MaTau, COUNT(*) FROM chongoi GROUP BY MaTau")
        total_seats_per_train = cursor.fetchall()
        conn.close()
        return total_seats_per_train

    def get_total_ticket_prices():
        conn = ketnoi()
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(GiaVe) FROM ve")
        total_ticket_prices = cursor.fetchone()[0]
        conn.close()
        return total_ticket_prices

    def get_total_customers_booking():
        conn = ketnoi()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(DISTINCT ma_kh) FROM ve")
        total_customers_booking = cursor.fetchone()[0]
        conn.close()
        return total_customers_booking

    total_customers = get_total_customers()
    total_trains = get_total_trains()
    total_seats_per_train = get_total_seats_per_train()
    total_ticket_prices = get_total_ticket_prices()
    total_customers_booking = get_total_customers_booking()

    # Thiết lập giao diện
    header = ['Mục', 'Giá trị']
    data = [
        ('Tổng số khách', total_customers),
        ('Tổng số tàu', total_trains),
        ('Tổng tiền giá vé', total_ticket_prices),
        ('Tổng khách đặt vé', total_customers_booking)
    ]

    for ma_tau, total_seats in total_seats_per_train:
        data.append((f'Tổng số ghế của tàu {ma_tau}', total_seats))

    tree = ttk.Treeview(frame_noidung, columns=header, show='headings', height=len(data))
    tree.grid(column=0, row=0, padx=59, pady=60)

    for col in header:
        tree.heading(col, text=col)
        tree.column(col, width=340, anchor='center')

    for row in data:
        tree.insert('', 'end', values=row)


