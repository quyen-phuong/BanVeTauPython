from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import database
import  re

def show_ChoNgoi(frame_noidung):
    for widget in frame_noidung.winfo_children():
        widget.destroy()

    def clear_entries():
        input_ma_tau.set('')
        input_so_cho_ngoi.delete(0, END)
        input_hang_ghe.set('')
        input_con_trong.set('')

    def ChonDuLieuBang(event):
        selected_row = table_cn.focus()
        data = table_cn.item(selected_row, 'values')
        ma_chon = data[0]
        clear_entries()
        input_ma_tau.set(data[1])
        input_so_cho_ngoi.insert(0, data[2])
        input_hang_ghe.set(data[3])
        input_con_trong.set(data[4])

    def search_cn():
        try:
            rows = database.search_cn(input_timkiem_cn.get())
            update_table(rows)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi tìm kiếm: {str(e)}")

    def them_cn():
        ma_tau = input_ma_tau.get()
        so_cho_ngoi = input_so_cho_ngoi.get()
        hang_ghe = input_hang_ghe.get()
        con_trong = input_con_trong.get()

        if ma_tau == "" or so_cho_ngoi == "" or hang_ghe == "" or con_trong == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return
        if hang_ghe not in ["Ghế thường", "Ghế VIP", "Khác"]:
            messagebox.showerror("Lỗi", "Hạng Ghế phải chọn từ danh sách: Ghế thường, Ghế VIP.")
            return
        if con_trong not in ["Có", "Không", "Khác"]:
            messagebox.showerror("Lỗi", "Chọn trống phải chọn từ danh sách: Có, Không.")
            return
        # Kiểm tra định dạng của so_cho_ngoi
        pattern = r"^C\d{3}$"  # Định dạng Cxxx, ví dụ: C001
        if not re.match(pattern, so_cho_ngoi):
            messagebox.showerror("Lỗi", "Số ghế phải theo định dạng 'Cxxx', ví dụ: 'C001'.")
            return

        try:
            # Kiểm tra xem mã tàu và số chỗ ngồi đã tồn tại chưa
            if database.check_ma_tau_and_so_cho_ngoi_exist(ma_tau, so_cho_ngoi):
                messagebox.showerror("Lỗi", f"Số ghế {so_cho_ngoi} đã tồn tại cho mã tàu {ma_tau}.")
                return

            # Thêm chỗ ngồi mới vào cơ sở dữ liệu
            success = database.them_chongoi(ma_tau, so_cho_ngoi, hang_ghe, con_trong)
            if success:
                messagebox.showinfo("Thông báo", f"Đã thêm số ghế {so_cho_ngoi} cho mã tàu {ma_tau}.")
                clear_entries()
                display_data()
            else:
                messagebox.showerror("Lỗi", "Thêm số ghế không thành công.")

        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi: {str(e)}")

    def sua_cn():
        try:
            selected_row = table_cn.focus()
            data = table_cn.item(selected_row, 'values')
            ma_chon = data[0]
            database.sua_cn(ma_chon, input_ma_tau.get(), input_so_cho_ngoi.get(), input_hang_ghe.get(), input_con_trong.get())
            messagebox.showinfo("Thông báo", "Cập nhật chỗ ngồi thành công")
            clear_entries()
            display_data()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi cập nhật chỗ ngồi: {str(e)}")

    def xoa_cn():
        try:
            selected_row = table_cn.focus()
            data = table_cn.item(selected_row, 'values')
            ma_chon = data[0]
            database.xoa_cn(ma_chon)
            messagebox.showinfo("Thông báo", "Xóa chỗ ngồi thành công")
            clear_entries()
            display_data()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi xóa chỗ ngồi: {str(e)}")

    def display_data():
        try:
            rows = database.Hien_Thi_CN()
            update_table(rows)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi hiển thị dữ liệu: {str(e)}")

    def update_table(rows):
        table_cn.delete(*table_cn.get_children())
        for row in rows:
            table_cn.insert("", END, values=row)

    def validate_entries():
        if not input_ma_tau.get():
            messagebox.showerror("Lỗi","Trường 'Mã tàu' không được để trống")
        if not input_so_cho_ngoi.get():
            messagebox.showerror("Lỗi","Trường 'Số chỗ ngồi' không được để trống")
        if not input_hang_ghe.get():
            messagebox.showerror("Lỗi","Trường 'Hạng ghế' không được để trống")
        if not input_con_trong.get():
            messagebox.showerror("Lỗi","Trường 'Còn trống' không được để trống")

    for widget in frame_noidung.winfo_children():
        widget.destroy()

    frame_tb = Frame(frame_noidung, bg="White")
    frame_tb.pack(side="top", fill="y")

    frame_chucnang = Frame(frame_noidung, width=300, height=200, bg="White")
    frame_chucnang.pack(side="bottom", fill="both", expand=True)

    frame_timkiem = Frame(frame_tb, bg="White")
    frame_timkiem.pack(side="top", pady=10)

    input_timkiem_cn = Entry(frame_timkiem, font=("Arial", 11), highlightbackground="light blue", highlightthickness=1,
                             borderwidth=0, width=30)
    input_timkiem_cn.grid(row=0, column=0, padx=10, pady=10)

    anh = Image.open(r'D:\BAITAPCACMON\BT-CODE\PY\btl_python\img\icontim.png')
    size = anh.resize((20, 20), Image.LANCZOS)
    global img
    img = ImageTk.PhotoImage(size)
    btn_timkiem_cn = Button(frame_timkiem, image=img, command=search_cn, borderwidth=0)
    btn_timkiem_cn.grid(row=0, column=1, padx=(0, 10))

    columns = ("Mã chỗ ngồi", "Mã tàu", "Số chỗ ngồi", "Hạng ghế", "Còn trống")
    table_cn = ttk.Treeview(frame_tb, columns=columns, show="headings")
    table_cn.heading("Mã chỗ ngồi", text="Mã chỗ ngồi")
    table_cn.heading("Mã tàu", text="Mã tàu")
    table_cn.heading("Số chỗ ngồi", text="Số chỗ ngồi")
    table_cn.heading("Hạng ghế", text="Hạng ghế")
    table_cn.heading("Còn trống", text="Còn trống")
    table_cn.column("Mã chỗ ngồi", minwidth=0, width=200)
    table_cn.column("Mã tàu", minwidth=0, width=200)
    table_cn.column("Số chỗ ngồi", minwidth=0, width=200)
    table_cn.column("Hạng ghế", minwidth=0, width=200)
    table_cn.column("Còn trống", minwidth=0, width=200)
    table_cn.pack(fill="both", expand=True)

    table_cn.bind("<ButtonRelease-1>", ChonDuLieuBang)
    ma_chon = None
    display_data()

    btn_them = Button(frame_chucnang, command=them_cn, text="Thêm", font=("Arial", 8, "bold"), fg="black", borderwidth=0,
                      bg="light blue", pady=6, padx=45)
    btn_them.place(x=5, y=30)
    btn_sua = Button(frame_chucnang, command=sua_cn, text="Sửa", font=("Arial", 8, "bold"), fg="black", borderwidth=0,
                     bg="light blue", pady=6, padx=45)
    btn_sua.place(x=150, y=30)
    btn_xoa = Button(frame_chucnang, command=xoa_cn, text="Xóa", font=("Arial", 8, "bold"), fg="black", borderwidth=0,
                     bg="light blue", pady=6, padx=45)
    btn_xoa.place(x=290, y=30)

    lb_ma_tau = Label(frame_chucnang, bg="White", text="Mã tàu", fg="black", font=("Arial", 10, "bold"))
    lb_ma_tau.place(x=5, y=70)
    ma_tau_values = database.get_ma_tau()  # Lấy danh sách mã tàu từ cơ sở dữ liệu
    input_ma_tau = ttk.Combobox(frame_chucnang, font=("Arial", 11), values=ma_tau_values, width=18)
    input_ma_tau.place(x=5, y=90)

    lb_so_cho_ngoi = Label(frame_chucnang, bg="White", text="Số chỗ ngồi", fg="black", font=("Arial", 10, "bold"))
    lb_so_cho_ngoi.place(x=200, y=70)
    input_so_cho_ngoi = Entry(frame_chucnang, font=("Arial", 11), highlightbackground="light blue", highlightthickness=1,
                          borderwidth=0, width=20)
    input_so_cho_ngoi.place(x=200, y=90)

    lb_hang_ghe = Label(frame_chucnang, bg="White", text="Hạng ghế", fg="black", font=("Arial", 10, "bold"))
    lb_hang_ghe.place(x=5, y=130)
    input_hang_ghe = ttk.Combobox(frame_chucnang, font=("Arial", 11), state="readonly", values=["Ghế thường", "Ghế VIP"], width=18)
    input_hang_ghe.place(x=5, y=150)

    lb_con_trong = Label(frame_chucnang, bg="White", text="Còn trống", fg="black", font=("Arial", 10, "bold"))
    lb_con_trong.place(x=200, y=130)
    input_con_trong = ttk.Combobox(frame_chucnang, font=("Arial", 11), state="readonly", values=["Có", "Không"], width=18)
    input_con_trong.place(x=200, y=150)
