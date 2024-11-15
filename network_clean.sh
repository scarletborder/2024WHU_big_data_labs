docker stop $(docker ps -aq)       # 停止所有容器
docker rm $(docker ps -aq)         # 删除所有容器
docker network rm $(docker network ls -q)  # 删除所有网络
