
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from tkcalendar import DateEntry
from datetime import datetime
import database

def show_LichTrinh(frame_noidung):
    for widget in frame_noidung.winfo_children():
        widget.destroy()

    def clear_entries():
        input_ma_tau.delete(0, END)
        input_so_cho_ngoi.delete(0, END)
        input_hang_ghe.delete(0, END)
        input_con_trong.delete(0, END)
        input_timeden_lt.delete(0, END)
        input_ngaykh_ghe.delete(0, END)
        input_ngayden_ghe.delete(0, END)
    def search_lichtrinh():
        try:
            keyword = input_timkiem_cn.get()
            rows = database.search_lichtrinh(keyword)
            update_table(rows)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi tìm kiếm: {str(e)}")

    def validate_dates():
        ngay_kh = input_ngaykh_ghe.get_date()
        ngay_den = input_ngayden_ghe.get_date()
        current_date = datetime.now().date()

        if ngay_kh < current_date:
            messagebox.showerror("Lỗi", "Ngày khởi hành không được trước ngày hiện tại.")
            return False

        if ngay_den < ngay_kh:
            messagebox.showerror("Lỗi", "Ngày đến phải bằng hoặc sau ngày khởi hành.")
            return False

        return True

    def them_lichtrinh():
        if not validate_dates():
            return
        try:
            ma_tau = input_ma_tau.get()
            ga_khoi_hanh = input_so_cho_ngoi.get()
            ga_den = input_hang_ghe.get()
            thoi_gian_khoi_hanh = input_con_trong.get()
            thoi_gian_den = input_timeden_lt.get()
            ngaykh_ghe = input_ngaykh_ghe.get().get_date()
            ngayden_ghe = input_ngayden_ghe.get().get_date()

            if len(ma_tau) == 0 or len(ga_khoi_hanh) == 0 or len(ga_den) == 0 or len(thoi_gian_khoi_hanh) == 0:
                messagebox.showerror("Lỗi","Vui lòng điền đầy đủ thông tin.")

            if database.check_lichtrinh_exist(ma_tau, ga_khoi_hanh, ga_den):
                messagebox.showerror("Lỗi","Lịch trình này đã tồn tại trong cơ sở dữ liệu.")

            database.them_lichtrinh(ma_tau, ga_khoi_hanh, ga_den, thoi_gian_khoi_hanh, thoi_gian_den, ngaykh_ghe, ngayden_ghe)
            messagebox.showinfo("Thông báo", "Thêm lịch trình thành công")
            clear_entries()
            display_data()

        except ValueError as ve:
            messagebox.showerror("Lỗi", str(ve))

        except Exception as e:
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin.")

    def sua_lichtrinh():
        try:
            selected_row = table_cn.focus()
            data = table_cn.item(selected_row, 'values')
            print("Selected Row:", selected_row)
            print("Data:", data)

            if not data:
                messagebox.showwarning("Cảnh báo", "Vui lòng chọn một lịch trình để sửa.")
                return

            ma_chon = data[0]  # Lấy mã lịch trình từ dữ liệu đã chọn
            ma_tau_moi = input_ma_tau.get()
            ga_khoi_hanh_moi = input_so_cho_ngoi.get()
            ga_den_moi = input_hang_ghe.get()
            thoi_gian_khoi_hanh_moi = input_con_trong.get()
            thoi_gian_den_moi = input_timeden_lt.get()
            ngaykh_ghe = input_ngaykh_ghe.get()
            ngayden_ghe = input_ngayden_ghe.get()

            # Thực hiện cập nhật thông tin vào database
            database.sua_lichtrinh(ma_chon, ma_tau_moi, ga_khoi_hanh_moi, ga_den_moi, thoi_gian_khoi_hanh_moi,
                                   thoi_gian_den_moi,ngaykh_ghe,ngayden_ghe)

            messagebox.showinfo("Thông báo", "Cập nhật lịch trình thành công")
            clear_entries()
            display_data()

        except IndexError:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một lịch trình để sửa.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi cập nhật lịch trình: {str(e)}")

    def xoa_lichtrinh():
        try:
            selected_row = table_cn.focus()
            data = table_cn.item(selected_row, 'values')
            ma_chon = data[0]
            database.xoa_lichtrinh(ma_chon)
            messagebox.showinfo("Thông báo", "Xóa lịch trình thành công")
            clear_entries()
            display_data()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi xóa lịch trình: {str(e)}")

    def ChonDuLieuBang(event):
        selected_row = table_cn.focus()
        data = table_cn.item(selected_row, 'values')
        ma_chon = data[0]
        clear_entries()
        input_ma_tau.insert(0, data[1])
        input_so_cho_ngoi.insert(0, data[3])
        input_hang_ghe.insert(0, data[4])
        input_con_trong.insert(0, data[5])
        input_timeden_lt.insert(0, data[6])
        input_ngaykh_ghe.insert(0, data[7])
        input_ngayden_ghe.insert(0, data[8])

    def display_data():
        try:
            rows = database.Hien_Thi_lichtrinh()
            update_table(rows)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi hiển thị dữ liệu: {str(e)}")

    def update_table(rows):
        table_cn.delete(*table_cn.get_children())
        for row in rows:
            table_cn.insert("", END, values=row)

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
    btn_timkiem_kh = Button(frame_timkiem, image=img, command=search_lichtrinh, borderwidth=0)
    btn_timkiem_kh.grid(row=0, column=1, padx=(0, 10))

    columns = ("Mã lịch trình", "Mã tàu", "Tên tàu", "Ga khởi hành", "Ga đến", "Thời gian khởi hành", "Thời gian đến", "Ngày Khởi Hành", "Ngày Đến")
    table_cn = ttk.Treeview(frame_tb, columns=columns, show="headings")
    table_cn.heading("Mã lịch trình", text="Mã lịch trình")
    table_cn.heading("Mã tàu", text="Mã tàu")
    table_cn.heading("Tên tàu", text="Tên tàu")
    table_cn.heading("Ga khởi hành", text="Ga khởi hành")
    table_cn.heading("Ga đến", text="Ga đến")
    table_cn.heading("Thời gian khởi hành", text="Thời gian khởi hành")
    table_cn.heading("Thời gian đến", text="Thời gian đến")
    table_cn.heading("Ngày Khởi Hành", text="Ngày Khởi Hành")
    table_cn.heading("Ngày Đến", text="Ngày Đến")
    table_cn.column("Mã lịch trình", minwidth=0, width=50)
    table_cn.column("Mã tàu", minwidth=0, width=50)
    table_cn.column("Tên tàu", minwidth=0, width=80)
    table_cn.column("Ga khởi hành", minwidth=0, width=180)
    table_cn.column("Ga đến", minwidth=0, width=180)
    table_cn.column("Thời gian khởi hành", minwidth=0, width=120)
    table_cn.column("Thời gian đến", minwidth=0, width=120)
    table_cn.column("Ngày Khởi Hành", minwidth=0, width=120)
    table_cn.column("Ngày Đến", minwidth=0, width=120)
    table_cn.pack(fill="both", expand=True)

    table_cn.bind("<ButtonRelease-1>", ChonDuLieuBang)
    ma_chon = None
    display_data()

    btn_them = Button(frame_chucnang, command=them_lichtrinh, text="Thêm", font=("Arial", 8, "bold"), fg="black", borderwidth=0,
                      bg="light blue", pady=6, padx=45)
    btn_them.place(x=5, y=30)
    btn_sua = Button(frame_chucnang, command=sua_lichtrinh, text="Sửa", font=("Arial", 8, "bold"), fg="black", borderwidth=0,
                     bg="light blue", pady=6, padx=45)
    btn_sua.place(x=150, y=30)
    btn_xoa = Button(frame_chucnang, command=xoa_lichtrinh, text="Xóa", font=("Arial", 8, "bold"), fg="black", borderwidth=0,
                     bg="light blue", pady=6, padx=45)
    btn_xoa.place(x=290, y=30)

    lb_ma_tau = Label(frame_chucnang, bg="White", text="Mã tàu", fg="black", font=("Arial", 10, "bold"))
    lb_ma_tau.place(x=5, y=70)
    ma_tau_values = database.get_ma_tau()
    input_ma_tau = ttk.Combobox(frame_chucnang, font=("Arial", 11), values=ma_tau_values, width=18)
    input_ma_tau.place(x=5, y=90)
    lb_so_cho_ngoi = Label(frame_chucnang, bg="White", text="Ga Khởi Hành", fg="black", font=("Arial", 10, "bold"))
    lb_so_cho_ngoi.place(x=200, y=70)
    input_so_cho_ngoi = Entry(frame_chucnang, font=("Arial", 11), highlightbackground="light blue", highlightthickness=1,
                          borderwidth=0, width=20)
    input_so_cho_ngoi.place(x=200, y=90)

    lb_hang_ghe = Label(frame_chucnang, bg="White", text="Ga Đến", fg="black", font=("Arial", 10, "bold"))
    lb_hang_ghe.place(x=5, y=130)
    input_hang_ghe =  Entry(frame_chucnang, font=("Arial", 11), highlightbackground="light blue", highlightthickness=1,
                          borderwidth=0, width=20)
    input_hang_ghe.place(x=5, y=150)

    lb_con_trong = Label(frame_chucnang, bg="White", text="Thời gian khởi hành", fg="black", font=("Arial", 10, "bold"))
    lb_con_trong.place(x=200, y=130)
    input_con_trong = ttk.Combobox(frame_chucnang, font=("Arial", 11), state="readonly", values=["01:00 PM", "02:00 PM", "03:00 PM","04:00 PM", "05:00 PM", "06:00 PM"
                                                                               ,"07:00 PM", "08:00 PM", "09:00 PM","10:00 PM", "11:00 PM", "12:00 PM"
                                                                               ,"01:00 AM", "02:00 AM", "03:00 AM","04:00 AM", "05:00 AM", "06:00 AM"
                                                                               ,"07:00 AM", "08:00 AM", "09:00 AM","10:00 AM", "11:00 AM", "12:00 AM"], width=18)
    input_con_trong.place(x=200, y=150)

    lb_timeden_lt = Label(frame_chucnang, bg="White", text="Thời gian Đến", fg="black", font=("Arial", 10, "bold"))
    lb_timeden_lt.place(x=395, y=70)
    input_timeden_lt = ttk.Combobox(frame_chucnang, font=("Arial", 11), state="readonly", values=["01:00 PM", "02:00 PM", "03:00 PM","04:00 PM", "05:00 PM", "06:00 PM"
                                                                               ,"07:00 PM", "08:00 PM", "09:00 PM","10:00 PM", "11:00 PM", "12:00 PM"
                                                                               ,"01:00 AM", "02:00 AM", "03:00 AM","04:00 AM", "05:00 AM", "06:00 AM"
                                                                               ,"07:00 AM", "08:00 AM", "09:00 AM","10:00 AM", "11:00 AM", "12:00 AM"], width=18)
    input_timeden_lt.place(x=395, y=90)
    lb_ngaykh_ghe = Label(frame_chucnang, bg="White", text="Ngày Khởi Hành", fg="black", font=("Arial", 10, "bold"))
    lb_ngaykh_ghe.place(x=395, y=130)
    input_ngaykh_ghe =  DateEntry(frame_chucnang, font=("Arial", 11), highlightbackground="light blue", highlightthickness=1,
                          borderwidth=0, width=20, state="readonly", date_pattern="dd/mm/yyyy")
    input_ngaykh_ghe.place(x=395, y=150)

    lb_ngayden_ghe = Label(frame_chucnang, bg="White", text="Ngày Đến", fg="black", font=("Arial", 10, "bold"))
    lb_ngayden_ghe.place(x=590, y=70)
    input_ngayden_ghe = DateEntry(frame_chucnang, font=("Arial", 11), highlightbackground="light blue",
                                 highlightthickness=1,
                                 borderwidth=0, width=20, state="readonly", date_pattern="dd/mm/yyyy")
    input_ngayden_ghe.place(x=590, y=90)



