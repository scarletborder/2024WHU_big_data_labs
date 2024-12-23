#!/bin/bash

# 定义 Proto 文件路径
PROTO_DIR=./proto
OUT_DIR=./proto

# 确保输出目录存在
mkdir -p ${OUT_DIR}

# 执行 protoc 编译
python -m grpc_tools.protoc \
    -I ${PROTO_DIR} \
    --python_out=${OUT_DIR} \
    --grpc_python_out=${OUT_DIR} \
    --descriptor_set_out=${OUT_DIR}/descriptor.pb \
    --include_imports \
    ${PROTO_DIR}/ett.proto

python fix_imports.py