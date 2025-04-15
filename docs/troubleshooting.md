# docs/troubleshooting.md - Xử lý lỗi thường gặp

## 1. Không truy cập được API
- Kiểm tra container api đã chạy: `docker ps`
- Xem log: `docker logs qwen-api`
- Kiểm tra port 8000 đã mở chưa

## 2. Prometheus/Grafana/Jaeger không lên
- Kiểm tra container prometheus/grafana/jaeger đã chạy
- Kiểm tra volume mapping đúng chưa (prometheus.yml, grafana_dashboard.json)
- Xem log: `docker logs prometheus`/`grafana`/`jaeger`

## 3. Jenkins build fail
- Kiểm tra credential DockerHub, email đã cấu hình đúng
- Xem log build trên Jenkins UI
- Kiểm tra Docker daemon, quyền user

## 4. K8s không scale đủ 3 replicas
- Kiểm tra manifest deployment.yaml
- Xem log pod: `kubectl logs <pod>`
- Kiểm tra resource limit, quota namespace

## 5. Không thấy metrics/tracing
- Kiểm tra Prometheus scrape target đúng chưa
- Kiểm tra Jaeger agent, exporter đã cấu hình đúng env

---

*Gặp lỗi khác, hãy kiểm tra log chi tiết và đọc lại README.md, changelog.md.*
