import os

def fix_imports(file_path, old_import, new_import):
    with open(file_path, "r") as f:
        content = f.read()
    content = content.replace(old_import, new_import)
    with open(file_path, "w") as f:
        f.write(content)

# 修改路径
base_dir = "proto"
files_to_fix = ["ett_pb2.py", "ett_pb2_grpc.py"]

for file_name in files_to_fix:
    file_path = os.path.join(base_dir, file_name)
    fix_imports(file_path, "import ett_pb2", "import proto.ett_pb2")
