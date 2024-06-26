import mysql.connector
from datetime import datetime
def ketnoi():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="quanlybanve"
    )
#khách Hàng
def Hien_Thi_KH():
    conn = ketnoi()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM khachhang")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_employee(keyword):
    conn = ketnoi()
    cursor = conn.cursor()
    sql = "SELECT * FROM khachhang WHERE ho_ten LIKE %s"  # Sửa đổi cú pháp SQL
    cursor.execute(sql, ('%' + keyword + '%',))  # Sửa đổi tham số truyền vào
    rows = cursor.fetchall()
    conn.close()
    return rows

def check_cccd_exist(cccd):
    conn = ketnoi()
    cursor = conn.cursor()
    cursor.execute("SELECT cccd FROM khachhang WHERE cccd = %s", (cccd,))
    row = cursor.fetchone()
    conn.close()
    return row is not None
def get_ma_kh():
    conn = ketnoi()
    cursor = conn.cursor()
    cursor.execute("SELECT ma_kh FROM khachhang")
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]
def them_kh(hoten, ngaysinh, sex, sdt,cccd, email, diachi):
    conn = ketnoi()
    cursor = conn.cursor()
    sql = "INSERT INTO khachhang (ho_ten,ngay_sinh, gioi_tinh, sdt,cccd, email,dia_chi) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (hoten, ngaysinh, sex, sdt,cccd, email, diachi)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()

def sua_kh(ma_kh,hoten, ngaysinh, sex, sdt,cccd, email, diachi):
    conn = ketnoi()
    cursor = conn.cursor()
    sql = "UPDATE khachhang SET ho_ten=%s, ngay_sinh=%s, gioi_tinh=%s, sdt=%s, cccd=%s, email=%s, dia_chi=%s WHERE ma_kh=%s"
    values = (hoten, ngaysinh, sex, sdt,cccd, email, diachi,ma_kh)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
def xoa_kh(ma_kh):
    conn = ketnoi()
    cursor = conn.cursor()
    sql = "DELETE FROM khachhang WHERE ma_kh=%s"
    cursor.execute(sql, (ma_kh,))
    conn.commit()
    conn.close()

#Chỗ Ngồi
def Hien_Thi_CN():
    conn = ketnoi()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM chongoi ORDER BY MaTau, SoChoNgoi")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_cn(keyword):
    conn = ketnoi()
    cursor = conn.cursor()
    sql = "SELECT * FROM chongoi WHERE SoChoNgoi LIKE %s ORDER BY MaTau, SoChoNgoi"
    cursor.execute(sql, ('%' + keyword + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def check_ma_tau_and_so_cho_ngoi_exist(ma_tau, so_cho_ngoi):
    conn = ketnoi()
    cursor = conn.cursor()
    query = "SELECT * FROM chongoi WHERE MaTau = %s AND SoChoNgoi = %s"
    cursor.execute(query, (ma_tau, so_cho_ngoi))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def them_chongoi(ma_tau, so_cho_ngoi, hang_ghe, con_trong):
    conn = ketnoi()
    cursor = conn.cursor()
    query = "INSERT INTO chongoi (MaTau, SoChoNgoi, HangGhe, ConTrong) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (ma_tau, so_cho_ngoi, hang_ghe, con_trong))
    conn.commit()
    conn.close()
    return True

def get_ma_chongoi():
    conn = ketnoi()
    cursor = conn.cursor()
    cursor.execute("SELECT MaChoNgoi FROM chongoi WHERE ConTrong = 1")
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]
def sua_cn(MaChoNgoi, MaTau, SoChoNgoi, HangGhe, ConTrong):
    conn = ketnoi()
    cursor = conn.cursor()
    sql = "UPDATE chongoi SET MaTau=%s, SoChoNgoi=%s, HangGhe=%s, ConTrong=%s WHERE MaChoNgoi=%s"
    values = (MaTau, SoChoNgoi, HangGhe, ConTrong, MaChoNgoi)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()

def xoa_cn(ma_cn):
    conn = ketnoi()
    cursor = conn.cursor()
    sql = "DELETE FROM chongoi WHERE MaChoNgoi=%s"
    cursor.execute(sql, (ma_cn,))
    conn.commit()
    conn.close()
#Chuyến tàu
def Hien_Thi_Tau():
    conn = ketnoi()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tau")
    rows = cursor.fetchall()
    conn.close()
    return rows
def search_tau(keyword):
    conn = ketnoi()
    cursor = conn.cursor()
    sql = "SELECT * FROM tau WHERE TenTau LIKE %s"  # Sửa đổi cú pháp SQL
    cursor.execute(sql, ('%' + keyword + '%',))  # Sửa đổi tham số truyền vào
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_ma_tau():
    conn = ketnoi()
    cursor = conn.cursor()
    cursor.execute("SELECT MaTau FROM tau")
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]

def them_tau(so_hieu_tau,ten_tau):
    conn = ketnoi()
    cursor = conn.cursor()
    sql = "INSERT INTO tau (SoHieuTau,TenTau) VALUES (%s, %s)"
    values = (so_hieu_tau,ten_tau)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()

def sua_tau(MaTau,so_hieu_tau,ten_tau):
    conn = ketnoi()
    cursor = conn.cursor()
    sql = "UPDATE tau SET SoHieuTau=%s,TenTau=%s WHERE MaTau=%s"
    values = (so_hieu_tau,ten_tau,MaTau)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()

def xoa_tau(ma_tau):
    conn = ketnoi()
    cursor = conn.cursor()
    sql = "DELETE FROM tau WHERE MaTau=%s"
    cursor.execute(sql, (ma_tau,))
    conn.commit()
    conn.close()

#Lịch trình
def Hien_Thi_lichtrinh():
    conn = ketnoi()
    cursor = conn.cursor()
    query = """
        SELECT 
            lt.MaLichTrinh,
            lt.MaTau,
            t.TenTau,
            lt.GaKhoiHanh,
            lt.GaDen,
            lt.ThoiGianKhoiHanh,
            lt.ThoiGianDen,
            lt.NgayKhoiHanh,
            lt.NgayDen
        FROM 
            LichTrinh lt 
        JOIN 
            Tau t ON lt.MaTau = t.MaTau
        ORDER BY 
            lt.MaTau
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_ma_lt():
    conn = ketnoi()
    cursor = conn.cursor()
    cursor.execute("SELECT MaLichTrinh FROM LichTrinh")
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]


def check_lichtrinh_exist(ma_tau, ga_khoi_hanh, ga_den):
    conn = ketnoi()
    cursor = conn.cursor()
    query = "SELECT * FROM LichTrinh WHERE MaTau = %s AND GaKhoiHanh = %s AND GaDen = %s"
    cursor.execute(query, (ma_tau, ga_khoi_hanh, ga_den))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def them_lichtrinh(ma_tau, ga_khoi_hanh, ga_den, thoi_gian_khoi_hanh, thoi_gian_den,NgayKhoiHanh,NgayDen):
    conn = ketnoi()
    cursor = conn.cursor()
    sql = """
        INSERT INTO LichTrinh (MaTau, GaKhoiHanh, GaDen, ThoiGianKhoiHanh, ThoiGianDen,NgayKhoiHanh,NgayDen)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (ma_tau, ga_khoi_hanh, ga_den, thoi_gian_khoi_hanh, thoi_gian_den,NgayKhoiHanh,NgayDen)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    return True

def search_lichtrinh(keyword):
    conn = ketnoi()
    cursor = conn.cursor()
    sql = """
        SELECT 
            lt.MaLichTrinh,
            lt.MaTau,
            t.TenTau,
            lt.GaKhoiHanh,
            lt.GaDen,
            lt.ThoiGianKhoiHanh,
            lt.ThoiGianDen,
            lt.NgayKhoiHanh,
            lt.NgayDen
        FROM 
            LichTrinh lt
        JOIN 
            Tau t ON lt.MaTau = t.MaTau
        WHERE 
            lt.GaKhoiHanh LIKE %s OR lt.GaDen LIKE %s
        ORDER BY 
            lt.MaTau
    """
    cursor.execute(sql, ('%' + keyword + '%', '%' + keyword + '%'))
    rows = cursor.fetchall()
    conn.close()
    return rows

def sua_lichtrinh(ma_lich_trinh, ma_tau_moi, ga_khoi_hanh_moi, ga_den_moi, thoi_gian_khoi_hanh_moi, thoi_gian_den_moi,NgayKhoiHanh,NgayDen):
    conn = ketnoi()
    cursor = conn.cursor()
    sql = """
        UPDATE LichTrinh
        SET MaTau = %s, GaKhoiHanh = %s, GaDen = %s, ThoiGianKhoiHanh = %s, ThoiGianDen = %s,NgayKhoiHanh = %s,NgayDen = %s
        WHERE MaLichTrinh = %s
    """
    values = (ma_tau_moi, ga_khoi_hanh_moi, ga_den_moi, thoi_gian_khoi_hanh_moi, thoi_gian_den_moi,NgayKhoiHanh,NgayDen, ma_lich_trinh)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()

def xoa_lichtrinh(ma_lichtrinh):
    conn = ketnoi()
    cursor = conn.cursor()
    sql = "DELETE FROM LichTrinh WHERE MaLichTrinh=%s"
    cursor.execute(sql, (ma_lichtrinh,))
    conn.commit()
    conn.close()

#Vé Tàu
def Hien_Thi_Ve():
    conn = ketnoi()
    cursor = conn.cursor()
    sql = """
        SELECT Ve.MaVe, KhachHang.ma_kh,LichTrinh.MaLichTrinh, ChoNgoi.MaChoNgoi,KhachHang.ho_ten, Tau.TenTau, LichTrinh.GaKhoiHanh, LichTrinh.GaDen,
               LichTrinh.ThoiGianKhoiHanh, LichTrinh.NgayKhoiHanh, ChoNgoi.SoChoNgoi, Ve.NgayDatVe, Ve.GiaVe, Ve.TrangThai
        FROM Ve
        INNER JOIN KhachHang ON Ve.ma_kh = KhachHang.ma_kh
        INNER JOIN LichTrinh ON Ve.MaLichTrinh = LichTrinh.MaLichTrinh
        INNER JOIN ChoNgoi ON Ve.MaChoNgoi = ChoNgoi.MaChoNgoi
        INNER JOIN Tau ON ChoNgoi.MaTau = Tau.MaTau
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_ve(keyword):
    conn = ketnoi()
    cursor = conn.cursor()
    sql = """
        SELECT Ve.MaVe, KhachHang.ma_kh,LichTrinh.MaLichTrinh, ChoNgoi.MaChoNgoi,KhachHang.ho_ten, Tau.TenTau, LichTrinh.GaKhoiHanh, LichTrinh.GaDen,
               LichTrinh.ThoiGianKhoiHanh, LichTrinh.NgayKhoiHanh, ChoNgoi.SoChoNgoi, Ve.NgayDatVe, Ve.GiaVe, Ve.TrangThai
        FROM Ve
        INNER JOIN KhachHang ON Ve.ma_kh = KhachHang.ma_kh
        INNER JOIN LichTrinh ON Ve.MaLichTrinh = LichTrinh.MaLichTrinh
        INNER JOIN ChoNgoi ON Ve.MaChoNgoi = ChoNgoi.MaChoNgoi
        INNER JOIN Tau ON ChoNgoi.MaTau = Tau.MaTau
        WHERE KhachHang.ho_ten LIKE %s OR KhachHang.ma_kh LIKE %s
    """
    keyword = '%' + keyword + '%'
    cursor.execute(sql, (keyword, keyword))
    rows = cursor.fetchall()
    conn.close()
    return rows

def them_ve(ma_kh, MaLichTrinh, MaChoNgoi, TrangThai):
    conn = ketnoi()
    cursor = conn.cursor()

    # Get the seat type for the given seat ID
    cursor.execute("SELECT HangGhe FROM chongoi WHERE MaChoNgoi = %s", (MaChoNgoi,))
    hang_ghe = cursor.fetchone()[0]

    # Set the price based on the seat type
    if hang_ghe == "Ghế thường":
        GiaVe = 10000
    elif hang_ghe == "Ghế VIP":
        GiaVe = 20000
    else:
        raise ValueError("Invalid seat type")

    NgayDatVe = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    sql = """
        INSERT INTO ve (ma_kh, MaLichTrinh, MaChoNgoi, NgayDatVe, GiaVe, TrangThai)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (ma_kh, MaLichTrinh, MaChoNgoi, NgayDatVe, GiaVe, TrangThai)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()

def sua_ve(ma_ve, ma_kh, MaLichTrinh, MaChoNgoi, TrangThai):
    conn = ketnoi()
    cursor = conn.cursor()

    # Get the seat type for the given seat ID
    cursor.execute("SELECT HangGhe FROM chongoi WHERE MaChoNgoi = %s", (MaChoNgoi,))
    hang_ghe = cursor.fetchone()[0]

    # Set the price based on the seat type
    if hang_ghe == "Ghế thường":
        GiaVe = 10000
    elif hang_ghe == "Ghế VIP":
        GiaVe = 20000
    else:
        raise ValueError("Invalid seat type")

    NgayDatVe = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    sql = """
        UPDATE ve
        SET ma_kh = %s, MaLichTrinh = %s, MaChoNgoi = %s, NgayDatVe = %s, GiaVe = %s, TrangThai = %s
        WHERE MaVe = %s
    """
    values = (ma_kh, MaLichTrinh, MaChoNgoi, NgayDatVe, GiaVe, TrangThai, ma_ve)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()

def xoa_ve(ma_ve):
    conn = ketnoi()
    cursor = conn.cursor()
    sql = "DELETE FROM Ve WHERE MaVe = %s"
    values = (ma_ve,)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()