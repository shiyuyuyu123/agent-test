import os
def run_command(cmd):
    # 这是一个严重的安全漏洞
    os.system("echo " + cmd)
