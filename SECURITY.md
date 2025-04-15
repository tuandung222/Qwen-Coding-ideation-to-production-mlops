# SECURITY.md - Hướng dẫn bảo mật cho project

## 1. Không commit secret vào code
- Sử dụng file .env (không commit), .env.example để hướng dẫn.
- Sử dụng Jenkins Credential Store cho CI/CD.

## 2. Quản lý credential
- Đổi password định kỳ, xóa credential không dùng.
- Phân quyền truy cập Jenkins, DockerHub, email.

## 3. Audit & monitoring
- Theo dõi log Jenkins, Docker, API, Prometheus.
- Thiết lập alert khi có truy cập bất thường.

## 4. Cập nhật package định kỳ
- Chạy `pip list --outdated`, cập nhật dependencies.

---

*Tuân thủ các hướng dẫn bảo mật để bảo vệ hệ thống và dữ liệu!*
