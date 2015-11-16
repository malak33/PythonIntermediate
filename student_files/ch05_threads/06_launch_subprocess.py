import subprocess

proc = subprocess.Popen(['python', '06_read_send.py'], shell=True,
                          stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)

value = 'this msg'
results, err = proc.communicate(value.encode())
print(results.decode())
