# test_health.sh - Script kiểm tra health toàn bộ hệ thống
#!/bin/bash
set -e

check() {
  url=$1
  name=$2
  echo -n "Checking $name... "
  if curl -s $url | grep 'ok'; then
    echo "OK"
  else
    echo "FAIL"
    exit 1
  fi
}

check http://localhost:8000/healthz "API"
echo "All health checks passed!"
