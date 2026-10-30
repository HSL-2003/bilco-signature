# Trình Tạo Chữ Ký Email Bilco (Chuẩn Outlook)

Ứng dụng web tạo chữ ký email chuyên nghiệp theo đúng chuẩn nhận diện thương hiệu Bilco, hỗ trợ sao chép định dạng Rich-Text vào Microsoft Outlook, Gmail, Apple Mail trong 1 click.

## Hướng Dẫn Deploy Lên Web Miễn Phí Trong 60 Giây

### Cách 1: Deploy lên Vercel bằng trình duyệt (Khuyên dùng - Không cần gõ lệnh)
1. Đăng nhập [vercel.com](https://vercel.com) (bằng tài khoản GitHub hoặc Google).
2. Chọn **Add New...** > **Project**.
3. Kéo thả thư mục dự án này (`hh`) vào Vercel (hoặc đẩy lên GitHub rồi nhấn Import).
4. Nhấn nút **Deploy**.
5. Nhận ngay link web có SSL miễn phí trọn đời (ví dụ: `https://bilco-signature.vercel.app`).
*(Có thể gắn tên miền công ty miễn phí trong mục Settings > Domains, ví dụ: `signature.bilco.com.vn`)*.

### Cách 2: Deploy bằng dòng lệnh qua npx (1 lệnh duy nhất)
Mở PowerShell tại thư mục này và gõ:
```powershell
npx vercel
```
Làm theo hướng dẫn trên màn hình (đăng nhập email), Vercel sẽ tự động build và trả về đường link web ngay lập tức.

### Cách 3: Deploy qua GitHub Pages
1. Khởi tạo Git và đẩy lên GitHub:
   ```powershell
   git init
   git add .
   git commit -m "Initial Bilco Signature App"
   git branch -M main
   git remote add origin https://github.com/<tai-khoan-cua-ban>/bilco-signature.git
   git push -u origin main
   ```
2. Trên GitHub, vào **Settings** > **Pages** > Chọn **Deploy from a branch** > branch `main` > Save.
3. Trang web sẽ online tại: `https://<tai-khoan-cua-ban>.github.io/bilco-signature/`.
