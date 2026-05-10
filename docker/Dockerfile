FROM python:3.12-slim

WORKDIR /app

# 系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# 安装依赖
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 拷贝项目
COPY . .

# 赋予启动脚本权限
RUN chmod +x docker/start.sh

CMD ["bash", "docker/start.sh"]