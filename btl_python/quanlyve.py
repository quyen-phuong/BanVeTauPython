from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import database

def show_Ve(frame_noidung):
    for widget in frame_noidung.winfo_children():
        widget.destroy()

    def clear_entries():
        input_ma_kh.delete(0, END)
        input_ma_lichtrinh.delete(0, END)
        input_ma_chongoi.delete(0, END)
        input_trang_thai.delete(0, END)

    def search_ve():
        try:
            keyword = input_timkiem_ve.get()
            rows = database.search_ve(keyword)
            update_table(rows)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi tìm kiếm: {str(e)}")

    def them_ve():
        try:
            ma_kh = input_ma_kh.get()
            ma_lichtrinh = input_ma_lichtrinh.get()
            ma_chongoi = input_ma_chongoi.get()
            trang_thai = input_trang_thai.get()

            if len(ma_kh) == 0 or len(ma_lichtrinh) == 0 or len(ma_chongoi) == 0:
                raise ValueError("Vui lòng điền đầy đủ thông tin.")

            database.them_ve(ma_kh, ma_lichtrinh, ma_chongoi, trang_thai)
            messagebox.showinfo("Thông báo", "Thêm vé thành công")
            clear_entries()
            display_data()

        except ValueError as ve:
            messagebox.showerror("Lỗi", str(ve))

        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi thêm vé: {str(e)}")

    def sua_ve():
        try:
            selected_row = table_ve.focus()
            data = table_ve.item(selected_row, 'values')

            if not data:
                messagebox.showwarning("Cảnh báo", "Vui lòng chọn một vé để sửa.")
                return

            ma_ve = data[0]  # Lấy mã vé từ dữ liệu đã chọn
            ma_kh = input_ma_kh.get()
            ma_lichtrinh = input_ma_lichtrinh.get()
            ma_chongoi = input_ma_chongoi.get()
            trang_thai = input_trang_thai.get()

            database.sua_ve(ma_ve, ma_kh, ma_lichtrinh, ma_chongoi, trang_thai)
            messagebox.showinfo("Thông báo", "Cập nhật vé thành công")
            clear_entries()
            display_data()

        except IndexError:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một vé để sửa.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi cập nhật vé: {str(e)}")

    def xoa_ve():
        try:
            selected_row = table_ve.focus()
            data = table_ve.item(selected_row, 'values')
            ma_ve = data[0]
            database.xoa_ve(ma_ve)
            messagebox.showinfo("Thông báo", "Xóa vé thành công")
            clear_entries()
            display_data()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi xóa vé: {str(e)}")

    def ChonDuLieuBang(event):
        selected_row = table_ve.focus()
        data = table_ve.item(selected_row, 'values')
        ma_ve = data[0]
        clear_entries()
        input_ma_kh.insert(0, data[1])
        input_ma_lichtrinh.insert(0, data[2])
        input_ma_chongoi.insert(0, data[3])
        input_trang_thai.insert(0, data[13])

    def InVe(event):
        selected_row = table_ve.focus()
        data = table_ve.item(selected_row, 'values')
        if not data:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn một vé để in.")
            return
        in_ve_window = Toplevel()
        in_ve_window.title("In vé")
        in_ve_window.geometry("800x400")


        # Đảm bảo đường dẫn đến hình ảnh là chính xác
        image_path = "D:/BAITAPCACMON/BT-CODE/PY/btl_python/img/backgroudIndex.jpg"
        try:
            image = Image.open(image_path)
            background_image = ImageTk.PhotoImage(image)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tải hình ảnh: {e}")
            return
        canvas = Canvas(in_ve_window, width=800, height=400)
        canvas.pack(fill="both", expand=True)
        image_width = image.width
        image_height = image.height
        x_center = (800 - image_width) // 2
        y_center = (400 - image_height) // 2
        canvas.create_image(x_center, y_center, anchor=NW, image=background_image)
        in_ve_window.background_image = background_image

        #  cửa sổ nằm ở phía trước
        in_ve_window.transient(frame_noidung)
        in_ve_window.lift()
        in_ve_window.grab_set()


        # Định dạng thông tin vé theo mẫu
        name1 = Label(in_ve_window,text="CÔNG TY CỔ VẬN TẢI", fg="black", font=("Arial", 12, "bold"), bg='White')
        name1.place(x=310, y = 50)
        name2 = Label(in_ve_window, text="ĐƯỜNG SÁT", fg="black", font=("Arial", 12, "bold"), bg='White')
        name2.place(x=316, y=70)
        lb_nhom = Label(in_ve_window, text="MR.", bg="white", fg="gray", font=("Arial", 12, "bold"))
        lb_nhom.place(x=420, y = 70)
        lb_nhom1 = Label(in_ve_window, text="QK", bg="white", fg="red", font=("Arial", 12, "bold"))
        lb_nhom1.place(x=450, y=70)
        info_text = f"""
        Mã vé/TicketID: {data[0]}
        Ga đi: {data[6]}
        Ga đến: {data[7]}
        Tàu/Train: {data[5]}
        Ngày đi/Date: {data[9]}
        Giờ đi/Time: {data[8]}
        Toa/Coach: {data[3]}
        Chỗ/Seat: {data[10]}
        Loại chỗ/Class: {data[13]}
        Loại vé/Ticket: Người lớn
        Họ tên/Name: {data[4]}
        Giá/Price: {data[12]} VNĐ
        """

        lb_ve_info = Label(in_ve_window, text=info_text, font=("Arial", 12), justify=LEFT, bg="white")
        canvas.create_window(400,220, window=lb_ve_info, anchor="center")
        btn_inve = Button(in_ve_window, command=lambda: messagebox.showinfo("Thông báo", "In vé thành công!"), text="In vé", font=("Arial", 7, "bold"), fg="black",
                          borderwidth=0, bg="light blue", pady=3, padx=29)
        btn_inve.place(y = 200)
        canvas.create_window(400, 370, window=btn_inve, anchor="center")

    def display_data():
        try:
            rows = database.Hien_Thi_Ve()
            update_table(rows)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi hiển thị dữ liệu: {str(e)}")

    def update_table(rows):
        table_ve.delete(*table_ve.get_children())
        for row in rows:
            table_ve.insert("", END, values=row)

    frame_tb = Frame(frame_noidung, bg="White")
    frame_tb.pack(side="top", fill="y")

    frame_chucnang = Frame(frame_noidung, width=300, height=200, bg="White")
    frame_chucnang.pack(side="bottom", fill="both", expand=True)

    frame_timkiem = Frame(frame_tb, bg="White")
    frame_timkiem.pack(side="top", pady=10)

    input_timkiem_ve = Entry(frame_timkiem, font=("Arial", 11), highlightbackground="light blue", highlightthickness=1, borderwidth=0, width=30)
    input_timkiem_ve.grid(row=0, column=0, padx=10, pady=10)

    anh = Image.open(r'D:\BAITAPCACMON\BT-CODE\PY\btl_python\img\icontim.png')
    size = anh.resize((20, 20), Image.LANCZOS)
    global img
    img = ImageTk.PhotoImage(size)
    btn_timkiem_ve = Button(frame_timkiem, image=img, command=search_ve, borderwidth=0)
    btn_timkiem_ve.grid(row=0, column=1, padx=(0, 10))

    columns = ("Mã vé", "Mã khách hàng","Mã lịch trình","Mã Ghế", "Tên khách hàng", "Tên tàu", "Ga khởi hành", "Ga đến", "Thời gian khởi hành", "Ngày Khởi Hành", "Số chỗ ngồi", "Ngày đặt vé", "Giá vé", "Trạng thái")
    table_ve = ttk.Treeview(frame_tb, columns=columns, show="headings")
    for col in columns:
        table_ve.heading(col, text=col)
        table_ve.column(col, minwidth=0, width=76)
    ma_ve = None
    table_ve.pack(fill="both", expand=True)
    table_ve.bind("<ButtonRelease-1>", ChonDuLieuBang)
    table_ve.bind("<Double-1>", InVe)

    display_data()

    btn_them = Button(frame_chucnang, command=them_ve, text="Thêm", font=("Arial", 8, "bold"), fg="black", borderwidth=0, bg="light blue", pady=6, padx=45)
    btn_them.place(x=5, y=30)
    btn_sua = Button(frame_chucnang, command=sua_ve, text="Sửa", font=("Arial", 8, "bold"), fg="black", borderwidth=0, bg="light blue", pady=6, padx=45)
    btn_sua.place(x=150, y=30)
    btn_xoa = Button(frame_chucnang, command=xoa_ve, text="Xóa", font=("Arial", 8, "bold"), fg="black", borderwidth=0, bg="light blue", pady=6, padx=45)
    btn_xoa.place(x=290, y=30)

    lb_ma_kh = Label(frame_chucnang, bg="White", text="Mã khách hàng", fg="black", font=("Arial", 10, "bold"))
    lb_ma_kh.place(x=5, y=70)
    ma_kh_values = database.get_ma_kh()
    input_ma_kh = ttk.Combobox(frame_chucnang, font=("Arial", 11), values=ma_kh_values, width=18)
    input_ma_kh.place(x=5, y=90)

    lb_ma_lichtrinh = Label(frame_chucnang, bg="White", text="Mã lịch trình", fg="black", font=("Arial", 10, "bold"))
    lb_ma_lichtrinh.place(x=240, y=70)
    ma_lichtrinh_values = database.get_ma_lt()
    input_ma_lichtrinh = ttk.Combobox(frame_chucnang, font=("Arial", 11), values=ma_lichtrinh_values, width=18)
    input_ma_lichtrinh.place(x=240, y=90)

    lb_ma_chongoi = Label(frame_chucnang, bg="White", text="Mã chỗ ngồi", fg="black", font=("Arial", 10, "bold"))
    lb_ma_chongoi.place(x=5, y=130)
    ma_chongoi_values = database.get_ma_chongoi()
    input_ma_chongoi = ttk.Combobox(frame_chucnang, font=("Arial", 11), values=ma_chongoi_values, width=18)
    input_ma_chongoi.place(x=5, y=150)

    lb_trang_thai = Label(frame_chucnang, bg="White", text="Trạng thái", fg="black", font=("Arial", 10, "bold"))
    lb_trang_thai.place(x=240, y=130)
    input_trang_thai = ttk.Combobox(frame_chucnang, font=("Arial", 11), state="readonly", values=('DaDat', 'ChuDat'), width=18)
    input_trang_thai.place(x=240, y=150)
