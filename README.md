# LOKKI Phone Store

Một website thương mại điện tử bán điện thoại di động được xây dựng bằng Django.

## Tính năng chính

### Quản lý sản phẩm
- Hiển thị sản phẩm theo thương hiệu
- Tìm kiếm sản phẩm 
- Xem chi tiết sản phẩm (thông số kỹ thuật, mô tả, giá)
- Hình ảnh sản phẩm

### Giỏ hàng
- Thêm/xóa sản phẩm
- Cập nhật số lượng
- Tính tổng tiền
- Miễn phí vận chuyển cho đơn hàng trên $500

### Quản lý người dùng  
- Đăng ký/đăng nhập
- Quản lý thông tin cá nhân
- Xem lịch sử đơn hàng
- Lưu giỏ hàng theo user

### Thanh toán
- Thu thập thông tin giao hàng
- Chọn phương thức thanh toán (COD/chuyển khoản)
- Xác nhận đơn hàng
- Theo dõi trạng thái đơn hàng

## Cài đặt

1. Clone repository:
```bash
git clone https://github.com/your-username/lokki-phone-store.git
cd lokki-phone-store
```

2. Thực hiện migrate:
```bash
python manage.py migrate
```

3. Tạo tài khoản admin:
```bash
python manage.py createsuperuser
```

4. Cài Đặt Pillow Chạy Sever
```bash
pip install Pillow
```

5. Chạy server:
```bash
python manage.py runserver
```

## Cấu trúc thư mục

```
phone_store/
├── manage.py
├── media/              # Media files
│   ├── brands/        # Logo thương hiệu
│   └── phones/        # Ảnh sản phẩm  
├── phone_store/        # Cấu hình project
└── store/              # App chính
    ├── models.py       # Database models
    ├── views.py       # Logic xử lý
    ├── urls.py        # URL routing  
    └── templates/     # HTML templates
```

# Models chính trong ứng dụng:
- Phone: Thông tin điện thoại (tên, giá, mô tả, hình ảnh...)
- Brand: Thương hiệu điện thoại
- Cart: Giỏ hàng người dùng
- Order: Đơn hàng
- OrderItem: Chi tiết đơn hàng
  
## Công nghệ sử dụng

- **Backend**: Django 4.2
- **Frontend**: 
  - Bootstrap 5
  - Font Awesome 5
  - JavaScript
- **Database**: SQLite
- **Khác**: 
  - Django Authentication
  - Django Forms
  - Django Messages
  - Django Forms
  - Pillow
    
## Chức Năng Admin
 - Quản lý sản phẩm và thương hiệu
 - Xử lý đơn hàng 
 - Cập nhật trạng thái đơn hàng
 - Quản lý người dùng
 - Báo cáo doanh thu
   
## Tác giả
LOKKI Team(HPN)

## Giấy phép
MIT License

# Liên Hệ
Email: lezidevwizard@gmail.com | Website: https://lokkiphone.com

@Bản Quyền Thuộc Về Đội Ngũ Lokki Team

# @copyright: Không Copy dưới mọi hình thức!!! Do not Reup
