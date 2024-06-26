# -- Tạo cơ sở dữ liệu
# CREATE DATABASE quanlybanve;
# 
# -- Sử dụng cơ sở dữ liệu vừa tạo
# USE quanlybanve;
# 
# -- Tạo bảng Tau (Tàu)
# CREATE TABLE Tau (
#     MaTau INT PRIMARY KEY AUTO_INCREMENT,
#     SoHieuTau VARCHAR(10) UNIQUE,
#     TenTau VARCHAR(100)
# );
# 
# -- Tạo bảng ChoNgoi (Chỗ ngồi)
# CREATE TABLE ChoNgoi (
#     MaChoNgoi INT PRIMARY KEY AUTO_INCREMENT,
#     MaTau INT,
#     SoChoNgoi VARCHAR(10),
#     HangGhe VARCHAR(50),
#     ConTrong BOOLEAN DEFAULT TRUE,
#     FOREIGN KEY (MaTau) REFERENCES Tau(MaTau)
# );
# 
# -- Tạo bảng LichTrinh (Lịch trình)
# CREATE TABLE LichTrinh (
#     MaLichTrinh INT PRIMARY KEY AUTO_INCREMENT,
#     MaTau INT,
#     GaKhoiHanh VARCHAR(100),
#     GaDen VARCHAR(100),
#     ThoiGianKhoiHanh VARCHAR(100),
#     ThoiGianDen VARCHAR(100),
#     NgayKhoiHanh VARCHAR(100),
#     NgayDen VARCHAR(100),
#     FOREIGN KEY (MaTau) REFERENCES Tau(MaTau)
# );
# 
# -- Tạo bảng Ve (Vé)
# CREATE TABLE Ve (
#     MaVe INT PRIMARY KEY AUTO_INCREMENT,
#     ma_kh INT,
#     MaLichTrinh INT,
#     MaChoNgoi INT,
#     NgayDatVe VARCHAR(50),
#     GiaVe INT,
#     TrangThai VARCHAR(50) DEFAULT 'DaDat',
#     FOREIGN KEY (ma_kh) REFERENCES KhachHang(ma_kh),
#     FOREIGN KEY (MaLichTrinh) REFERENCES LichTrinh(MaLichTrinh),
#     FOREIGN KEY (MaChoNgoi) REFERENCES ChoNgoi(MaChoNgoi)
# );
# 
# -- Tạo bảng KhachHang (Khách hàng)
# CREATE TABLE KhachHang (
#     ma_kh INT AUTO_INCREMENT PRIMARY KEY,
#     ho_ten VARCHAR(255),
#     ngay_sinh DATE,
#     gioi_tinh VARCHAR(10),
#     sdt VARCHAR(15),
#     cccd INT UNIQUE,
#     email VARCHAR(255),
#     dia_chi VARCHAR(255)
# );
# 
# -- Tạo bảng TaiKhoan (Tài khoản)
# CREATE TABLE TaiKhoan (
#     ma_tk INT AUTO_INCREMENT PRIMARY KEY,
#     email VARCHAR(255),
#     tk VARCHAR(50) UNIQUE,
#     mk VARCHAR(50)
# );