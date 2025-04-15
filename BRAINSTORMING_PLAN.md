# Brainstorming & Phác thảo chiến lược đồ án MLOps: Qwen Coding Use Case

## 1. Mục tiêu tổng thể
- Biến ứng dụng Coding Multiple Choice QA (Qwen2.5-Coder-1.5B-Instruct) thành hệ thống MLOps production-ready.
- Tích hợp: FastAPI, Docker Compose, Prometheus, Grafana, Jaeger, Jenkins, Kubernetes, Helm, Cloud.

## 2. Chiến lược triển khai
### Giai đoạn 1: Chuẩn hóa codebase & API hóa
- Refactor code, tách inference thành FastAPI service.
- Đảm bảo API trả về đúng, có test case.

### Giai đoạn 2: Đóng gói & CI/CD
- Viết Dockerfile, docker-compose cho API, UI, monitoring.
- Viết Jenkinsfile: build, test, lint, build image, push image, deploy.

### Giai đoạn 3: Monitoring & Observability
- Tích hợp Prometheus, Grafana, Jaeger, OpenTelemetry.

### Giai đoạn 4: Scaling & Cloud Native
- Viết manifest K8s/Helm, deploy API 3 replicas, monitoring trên k8s.
- Deploy cloud.

### Giai đoạn 5: Báo cáo, sáng tạo, polish
- Viết tài liệu, dashboard, changelog, hướng dẫn sử dụng, troubleshooting.

## 3. Công nghệ & tài nguyên
- Python, FastAPI, Streamlit, pytest, flake8, Docker Compose, Jenkins, Prometheus, Grafana, Jaeger, K8s, Helm, Cloud, GitHub/GitLab.

## 4. Jenkins trong đồ án
- CI/CD: lint, test, build image, push, deploy, notification, artifact, security, monitoring pipeline, scaling agent.

## 5. Checklist hoàn thành
- [ ] FastAPI API đúng, test case đủ
- [ ] Docker Compose đủ service
- [ ] Jenkinsfile CI/CD hoàn chỉnh
- [ ] Prometheus + Grafana + Jaeger hoạt động
- [ ] K8s deploy 3 replicas, monitoring Helm
- [ ] Báo cáo, dashboard, changelog, tài liệu
- [ ] Cloud, autoscaling, model registry

---

*Bản phác thảo này là kim chỉ nam cho toàn bộ quá trình triển khai, giúp bám sát mục tiêu, công nghệ, checklist và chiến lược thực hiện đồ án MLOps hiện đại.*
