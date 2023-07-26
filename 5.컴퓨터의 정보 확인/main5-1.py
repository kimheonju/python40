import psutil

cpu = psutil.cpu_freq()
print('cpu정보:',cpu)

cpu_core = psutil.cpu_count(logical=False)
print('core의 수: ', cpu_core)

memory = psutil.virtual_memory()
print('메모리 용량: ',memory)

disk = psutil.disk_partitions()
print('디스크: ', disk)

net = psutil.net_io_counters()
print('네트워크 :', net)
