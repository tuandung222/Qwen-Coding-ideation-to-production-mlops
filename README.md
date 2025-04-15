# Qwen Coding Use Case - MLOps Project

## Tổng quan
Đồ án MLOps triển khai hệ thống Coding Multiple Choice Question Answering sử dụng mô hình Qwen2.5-Coder-1.5B-Instruct, tích hợp FastAPI, Docker Compose, Prometheus, Grafana, Jaeger, Jenkins CI/CD, Kubernetes, Helm, cloud-ready.

## Cấu trúc thư mục
```
qwen_coding_use_case/
├── src/                  # Source code FastAPI, model inference, metrics, tracing
│   ├── main.py
│   ├── model.py
│   ├── metrics.py
│   └── tracing.py
├── streamlit_ui/         # (Optional) Streamlit UI giữ lại nếu cần
│   └── app.py
├── tests/                # Unit test, API test
│   └── test_api.py
├── requirements.txt      # Python dependencies
├── Dockerfile            # Build FastAPI service
├── docker-compose.yml    # Compose all services: api, ui, prometheus, grafana, jaeger
├── Jenkinsfile           # CI/CD pipeline
├── k8s/                  # K8s manifest, Helm chart
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── prometheus.yaml
│   ├── grafana.yaml
│   └── jaeger.yaml
├── monitoring/           # Prometheus, Grafana, Jaeger config
│   ├── prometheus.yml
│   └── grafana_dashboard.json
├── docs/                 # Tài liệu, changelog, hướng dẫn sử dụng
│   ├── README.md
│   ├── changelog.md
│   └── troubleshooting.md
└── .pre-commit-config.yaml # Lint, format, security check
```

## Hướng dẫn sử dụng
- Xem docs/README.md để biết cách chạy local, CI/CD, deploy k8s, cloud.
- Xem Jenkinsfile để biết pipeline tự động hóa.
- Xem monitoring/ để cấu hình Prometheus, Grafana, Jaeger.

## Ghi chú
- Mỗi file sẽ có hướng dẫn chi tiết, code mẫu, dễ mở rộng.
- Đáp ứng đầy đủ các tiêu chí MLOps, monitoring, scaling, security, cloud-ready.

---
# Qwen-Coding-ideation-to-production-mlops
