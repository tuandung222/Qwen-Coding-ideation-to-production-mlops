# run_all.sh - Script khởi động toàn bộ hệ thống local
#!/bin/bash
set -e

echo "[+] Building and starting all services with Docker Compose..."
docker-compose up --build -d

echo "[+] Waiting for API to be ready..."
for i in {1..10}; do
  if curl -s http://localhost:8000/healthz | grep 'ok'; then
    echo "[+] API is up!"
    break
  fi
  sleep 2
done

echo "[+] Opening Streamlit UI (if needed)..."
streamlit run streamlit_ui/app.py &

echo "[+] All services started."
