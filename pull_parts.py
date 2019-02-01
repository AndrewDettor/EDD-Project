import subprocess


general_specs = "systeminfo"
get_cpu_info = "wmic cpu get name"
get_gpu_info = "wmic path win32_VideoController get name"
get_RAM_info = "wmic MEMORYCHIP get BankLabel, DeviceLocator, MemoryType, TypeDetail, Capacity, Speed"
get_drive_capacity = "wmic logicaldisk get size,freespace,caption"
get_drive_names = "wmic diskdrive get caption"


output = subprocess.call(get_cpu_info, shell=True)

print(type(output))
