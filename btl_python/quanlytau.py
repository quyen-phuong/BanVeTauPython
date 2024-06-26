from tkinter.ttk import *
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import database

def show_Tau(frame_noidung):
    def clear_entries():
        input_ten_tau.delete(0, END)
        input_loai_tau.delete(0, END)

    def ChonDuLieuBang(event):
        selected_row = table_kh.focus()
        data = table_kh.item(selected_row, 'values')
        ma_chon = data[0]
        clear_entries()
        input_loai_tau.insert(0, data[1])
        input_ten_tau.insert(0, data[2])


    def search_tau():
        try:
            rows = database.search_tau(input_timkiem_tau.get())
            update_table(rows)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi tìm kiếm: {str(e)}")

    def them_tau():
        try:
            loai_tau = input_loai_tau.get()
            ten_tau = input_ten_tau.get()

            if loai_tau == "" or ten_tau == "" :
                messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
                return
            if len(loai_tau) < 5:
                messagebox.showerror("Lỗi","Số hiệu tàu phải có ít nhất 5 ký tự")

            database.them_tau(loai_tau, ten_tau)
            messagebox.showinfo("Thông báo", "Thêm tàu thành công")
            clear_entries()
            display_data()

        except ValueError as ve:
            messagebox.showerror("Lỗi", str(ve))

        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi thêm tàu: {str(e)}")

    def sua_tau():
        try:
            selected_row = table_kh.focus()
            data = table_kh.item(selected_row, 'values')
            ma_chon = data[0]
            database.sua_tau(ma_chon, input_loai_tau.get(),input_ten_tau.get())
            messagebox.showinfo("Thông báo", "Cập nhật tàu thành công")
            clear_entries()
            display_data()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi cập nhật tàu: {str(e)}")

    def xoa_tau():
        try:
            selected_row = table_kh.focus()
            data = table_kh.item(selected_row, 'values')
            ma_chon = data[0]
            database.xoa_tau(ma_chon)
            messagebox.showinfo("Thông báo", "Xóa tàu thành công")
            clear_entries()
            display_data()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi xóa tàu: {str(e)}")

    def display_data():
        try:
            rows = database.Hien_Thi_Tau()
            update_table(rows)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi hiển thị dữ liệu: {str(e)}")

    def update_table(rows):
        table_kh.delete(*table_kh.get_children())
        for row in rows:
            table_kh.insert("", END, values=row)

    for widget in frame_noidung.winfo_children():
        widget.destroy()

    frame_tb = Frame(frame_noidung, bg="White")
    frame_tb.pack(side="top", fill="y")

    frame_chucnang = Frame(frame_noidung, width=300, height=200, bg="White")
    frame_chucnang.pack(side="bottom", fill="both", expand=True)

    frame_timkiem = Frame(frame_tb, bg="White")
    frame_timkiem.pack(side="top", pady=10)

    input_timkiem_tau = Entry(frame_timkiem, font=("Arial", 11), highlightbackground="light blue", highlightthickness=1,
                             borderwidth=0, width=30)
    input_timkiem_tau.grid(row=0, column=0, padx=10, pady=10)

    anh = Image.open(r'D:\BAITAPCACMON\BT-CODE\PY\btl_python\img\icontim.png')
    size = anh.resize((20, 20), Image.LANCZOS)
    global img
    img = ImageTk.PhotoImage(size)
    btn_timkiem_tau = Button(frame_timkiem, image=img, command=search_tau, borderwidth=0)
    btn_timkiem_tau.grid(row=0, column=1, padx=(0, 10))

    columns = ("Mã tàu", "Số hiệu tàu", "Tên tàu")
    table_kh = ttk.Treeview(frame_tb, columns=columns, show="headings")
    table_kh.heading("Mã tàu", text="Mã tàu")
    table_kh.heading("Số hiệu tàu", text="Số hiệu tàu")
    table_kh.heading("Tên tàu", text="Tên tàu")
    table_kh.column("Mã tàu", minwidth=0, width=300)
    table_kh.column("Số hiệu tàu", minwidth=0, width=300)
    table_kh.column("Tên tàu", minwidth=0, width=300)
    table_kh.pack(fill="both", expand=True)

    table_kh.bind("<ButtonRelease-1>", ChonDuLieuBang)
    ma_chon = None
    display_data()

    btn_them = Button(frame_chucnang, command=them_tau, text="Thêm", font=("Arial", 8, "bold"), fg="black", borderwidth=0,
                      bg="light blue", pady=6, padx=45)
    btn_them.place(x=5, y=30)
    btn_sua = Button(frame_chucnang, command=sua_tau, text="Sửa", font=("Arial", 8, "bold"), fg="black", borderwidth=0,
                     bg="light blue", pady=6, padx=45)
    btn_sua.place(x=150, y=30)
    btn_xoa = Button(frame_chucnang, command=xoa_tau, text="Xóa", font=("Arial", 8, "bold"), fg="black", borderwidth=0,
                     bg="light blue", pady=6, padx=45)
    btn_xoa.place(x=290, y=30)

    lb_ten_tau = Label(frame_chucnang, bg="White", text="Tên tàu", fg="black", font=("Arial", 10, "bold"))
    lb_ten_tau.place(x=5, y=70)
    input_ten_tau = Entry(frame_chucnang, font=("Arial", 11), highlightbackground="light blue", highlightthickness=1,
                         borderwidth=0, width=20)
    input_ten_tau.place(x=5, y=90)

    lb_loai_tau = Label(frame_chucnang, bg="White", text="Số hiệu tàu", fg="black", font=("Arial", 10, "bold"))
    lb_loai_tau.place(x=200, y=70)
    input_loai_tau = Entry(frame_chucnang, font=("Arial", 11), highlightbackground="light blue", highlightthickness=1,
                          borderwidth=0, width=20)
    input_loai_tau.place(x=200, y=90)