from cgitb import text
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from tkcalendar import DateEntry
from datetime import datetime
import re
import database

def show_KhachHang(frame_noidung):
    def clear_entries():
        input_ten_kh.delete(0, END)
        input_ngay_kh.set_date(datetime.now())  # Reset DateEntry to current date
        input_sex_kh.set('')
        input_sdt_kh.delete(0, END)
        input_cccd_kh.delete(0, END)
        input_email_kh.delete(0, END)
        input_diachi_kh.delete(0, END)

    def ChonDuLieuBang(event):
        selected_row = table_kh.focus()
        data = table_kh.item(selected_row, 'values')
        ma_chon = data[0]
        clear_entries()
        input_ten_kh.insert(0, data[1])
        input_ngay_kh.set_date(datetime.strptime(data[2], "%Y-%m-%d"))  # Set DateEntry value
        input_sex_kh.set(data[3])
        input_sdt_kh.insert(0, data[4])
        input_cccd_kh.insert(0, data[5])
        input_email_kh.insert(0, data[6])
        input_diachi_kh.insert(0, data[7])

    def search_employee():
        try:
            rows = database.search_employee(input_timkiem_kh.get())
            update_table(rows)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi tìm kiếm: {str(e)}")

    def them():
        # Lấy giá trị từ các trường nhập liệu
        ten_kh = input_ten_kh.get()
        ngay_sinh = input_ngay_kh.get_date().strftime("%Y-%m-%d")  # Convert DateEntry value to string
        gioi_tinh = input_sex_kh.get()
        sdt = input_sdt_kh.get()
        cccd = input_cccd_kh.get()
        email = input_email_kh.get()
        dia_chi = input_diachi_kh.get()

        if ten_kh == "" or ngay_sinh == "" or gioi_tinh == "" or sdt == ""\
                or cccd  == "" or email == "" or dia_chi == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return
        # Kiểm tra điều kiện nhập liệu
        if not re.match(r"^0\d{9}$", sdt):
            messagebox.showerror("Lỗi", "Số điện thoại phải có 10 chữ số và bắt đầu bằng 0.")
            return

        if gioi_tinh not in ["Nam", "Nữ", "Khác"]:
            messagebox.showerror("Lỗi", "Giới tính phải chọn từ danh sách: Nam, Nữ, Khác.")
            return

        if not re.match(r"^\d{12}$", cccd):
            messagebox.showerror("Lỗi", "CCCD phải có 12 chữ số và không chứa chữ cái.")
            return

        if database.check_cccd_exist(cccd):
            messagebox.showerror("Lỗi", "CCCD đã tồn tại trong cơ sở dữ liệu.")
            return

        try:
            dob = datetime.strptime(ngay_sinh, "%Y-%m-%d")
            age = (datetime.now() - dob).days // 365
            if age < 18:
                messagebox.showerror("Lỗi", "Khách hàng phải từ 18 tuổi trở lên.")
                return
        except ValueError:
            messagebox.showerror("Lỗi", "Định dạng ngày sinh không hợp lệ. Định dạng đúng là YYYY-MM-DD.")
            return

        # Kiểm tra email: phải có đuôi @gmail.com
        if not email.endswith("@gmail.com"):
            messagebox.showerror("Lỗi", "Email phải có đuôi @gmail.com.")
            return

        try:
            # Thêm khách hàng vào cơ sở dữ liệu
            database.them_kh(ten_kh, ngay_sinh, gioi_tinh, int(sdt), int(cccd), email, dia_chi)
            messagebox.showinfo("Thông báo", "Thêm khách hàng thành công")
            clear_entries()
            display_data()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi thêm khách hàng: {str(e)}")

    def sua():
        try:
            selected_row = table_kh.focus()
            data = table_kh.item(selected_row, 'values')
            ma_chon = data[0]
            ngay_sinh = input_ngay_kh.get_date().strftime("%Y-%m-%d")  # Convert DateEntry value to string
            database.sua_kh(ma_chon, input_ten_kh.get(), ngay_sinh, input_sex_kh.get(), int(input_sdt_kh.get()),
                            int(input_cccd_kh.get()), input_email_kh.get(), input_diachi_kh.get())
            messagebox.showinfo("Thông báo", "Cập nhật khách hàng thành công")
            clear_entries()
            display_data()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi cập nhật khách hàng: {str(e)}")

    def xoa():
        try:
            selected_row = table_kh.focus()
            data = table_kh.item(selected_row, 'values')
            ma_chon = data[0]
            database.xoa_kh(ma_chon)
            messagebox.showinfo("Thông báo", "Xóa khách hàng thành công")
            clear_entries()
            display_data()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi xóa khách hàng: {str(e)}")

    def display_data():
        try:
            rows = database.Hien_Thi_KH()
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

    input_timkiem_kh = Entry(frame_timkiem, font=("Arial", 11), highlightbackground="light blue", highlightthickness=1,
                             borderwidth=0, width=30)
    input_timkiem_kh.grid(row=0, column=0, padx=10, pady=10)

    anh = Image.open(r'D:\BAITAPCACMON\BT-CODE\PY\btl_python\img\icontim.png')
    size = anh.resize((20, 20), Image.LANCZOS)
    global img
    img = ImageTk.PhotoImage(size)
    btn_timkiem_kh = Button(frame_timkiem, image=img, command=search_employee, borderwidth=0)
    btn_timkiem_kh.grid(row=0, column=1, padx=(0, 10))

    columns = ("ma_kh", "Họ và tên", "Ngày Sinh", "Giới Tính", "Số điện thoại", "CCCD", "Email", "Địa Chỉ")
    table_kh = ttk.Treeview(frame_tb, columns=columns, show="headings")
    table_kh.heading("ma_kh", text="ID")
    table_kh.heading("Họ và tên", text="Tên NV")
    table_kh.heading("Ngày Sinh", text="Ngày Sinh")
    table_kh.heading("Giới Tính", text="Giới Tính")
    table_kh.heading("Số điện thoại", text="SĐT")
    table_kh.heading("CCCD", text="CCCD")
    table_kh.heading("Email", text="Email")
    table_kh.heading("Địa Chỉ", text="Địa Chỉ")
    table_kh.column("ma_kh", minwidth=0, width=50)
    table_kh.column("Họ và tên", minwidth=0, width=150)
    table_kh.column("Ngày Sinh", minwidth=0, width=100)
    table_kh.column("Giới Tính", minwidth=0, width=80)
    table_kh.column("Số điện thoại", minwidth=0, width=120)
    table_kh.column("CCCD", minwidth=0, width=100)
    table_kh.column("Email", minwidth=0, width=150)
    table_kh.column("Địa Chỉ", minwidth=0, width=250)
    table_kh.pack(fill="both", expand=True)
    table_kh.bind("<ButtonRelease-1>", ChonDuLieuBang)
    ma_chon = None
    display_data()

    btn_them = Button(frame_chucnang, command=them, text="Thêm", font=("Arial", 8, "bold"), fg="black", borderwidth=0,
                      bg="light blue", pady=6, padx=45)
    btn_them.place(x=5, y=30)
    btn_sua = Button(frame_chucnang, command=sua, text="Sửa", font=("Arial", 8, "bold"), fg="black", borderwidth=0,
                     bg="light blue", pady=6, padx=45)
    btn_sua.place(x=150, y=30)
    btn_xoa = Button(frame_chucnang, command=xoa, text="Xóa", font=("Arial", 8, "bold"), fg="black", borderwidth=0,
                     bg="light blue", pady=6, padx=45)
    btn_xoa.place(x=290, y=30)

    lb_ten_kh = Label(frame_chucnang, bg="White", text="Tên khách hàng", fg="black", font=("Arial", 10, "bold"))
    lb_ten_kh.place(x=5, y=70)
    input_ten_kh = Entry(frame_chucnang, font=("Arial", 11), highlightbackground="light blue", highlightthickness=1,
                         borderwidth=0, width=20)
    input_ten_kh.place(x=5, y=90)
    lb_ngay_kh = Label(frame_chucnang, bg="White", text="Ngày sinh", fg="black", font=("Arial", 10, "bold"))
    lb_ngay_kh.place(x=5, y=120)
    input_ngay_kh = DateEntry(frame_chucnang, font=("Arial", 11), date_pattern="y-mm-dd", highlightbackground="light blue", highlightthickness=1,
                          borderwidth=0, width=20)
    input_ngay_kh.place(x=5, y=140)

    lb_sex_kh = Label(frame_chucnang, bg="White", text="Giới tính", fg="black", font=("Arial", 10, "bold"))
    lb_sex_kh.place(x=200, y=70)
    input_sex_kh = ttk.Combobox(frame_chucnang, state="readonly", font=("Arial", 11), width=18, values=('Nam', 'Nữ'))
    input_sex_kh.place(x=200, y=90)

    lb_sdt_kh = Label(frame_chucnang, bg="White", text="Số điện thoại", fg="black", font=("Arial", 10, "bold"))
    lb_sdt_kh.place(x=200, y=120)
    input_sdt_kh = Entry(frame_chucnang, bg="White", font=("Arial", 11), highlightbackground="light blue", highlightthickness=1,
                         borderwidth=0, width=20)
    input_sdt_kh.place(x=200, y=140)

    lb_cccd_kh = Label(frame_chucnang, bg="White", text="Chứng minh thư", fg="black", font=("Arial", 10, "bold"))
    lb_cccd_kh.place(x=395, y=70)
    input_cccd_kh = Entry(frame_chucnang, bg="White", font=("Arial", 11), highlightbackground="light blue", highlightthickness=1,
                          borderwidth=0, width=20)
    input_cccd_kh.place(x=395, y=90)

    lb_email_kh = Label(frame_chucnang, bg="White", text="Email", fg="black", font=("Arial", 10, "bold"))
    lb_email_kh.place(x=395, y=120)
    input_email_kh = Entry(frame_chucnang, font=("Arial", 11), highlightbackground="light blue", highlightthickness=1,
                           borderwidth=0, width=20)
    input_email_kh.place(x=395, y=140)

    lb_diachi_kh = Label(frame_chucnang, bg="White", text="Địa chỉ", fg="black", font=("Arial", 10, "bold"))
    lb_diachi_kh.place(x=590, y=70)
    input_diachi_kh = Entry(frame_chucnang, font=("Arial", 11), highlightbackground="light blue", highlightthickness=1,
                            borderwidth=0, width=20)
    input_diachi_kh.place(x=590, y=90)
