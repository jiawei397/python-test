import psutil

count = psutil.cpu_count()  # CPU逻辑数量

print(count)

logicalCount = psutil.cpu_count(logical=False) # CPU物理核心
print(logicalCount)

cpu_times = psutil.cpu_times()
print(cpu_times)

virtual_memory = psutil.virtual_memory()
print(virtual_memory)

disk_partitions = psutil.disk_partitions() # 磁盘分区信息
print(disk_partitions)

usage = psutil.disk_usage('/')  # 磁盘使用情况
print(usage)
