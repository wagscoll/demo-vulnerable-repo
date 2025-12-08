import hashlib
import subprocess
import yaml

# 1. Hardcoded password
PASSWORD = "theCakeIsALie"

# 2. Insecure hash function
def bad_hash(data):
    return hashlib.md5(data.encode()).hexdigest()

# 3. Insecure subprocess usage (shell=True)
def run_system(cmd):
    return subprocess.Popen(cmd, shell=True)

# 4. Unsafe YAML load
def load_config(path):
    with open(path, "r") as f:
        return yaml.load(f, Loader=yaml.Loader)

# 5. eval-based code execution
def execute_user_input(expr):
    return eval(expr)

# Trigger the vulnerabilities
print(bad_hash("hello"))
run_system("ls -la")
