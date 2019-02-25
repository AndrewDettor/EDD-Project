import subprocess


def getGPUname():
    get_gpu_info = "wmic path win32_VideoController get name"
    return subprocess.call(get_gpu_info, shell=True)


def getCPUname():
    get_cpu_info = "wmic cpu get name"
    return subprocess.call(get_cpu_info, shell=True)


def getRAMinfo():
    get_RAM_info = "wmic MEMORYCHIP get BankLabel, DeviceLocator, MemoryType, TypeDetail, Capacity, Speed"
    return subprocess.call(get_RAM_info, shell=True)


def getDriveCapacity():
    get_drive_capacity = "wmic logicaldisk get size,freespace,caption"
    return subprocess.call(get_drive_capacity, shell=True)


def getDrivenames():
    get_drive_names = "wmic diskdrive get caption"
    return subprocess.call(get_drive_names, shell=True)


print(getGPUname())
print('\n\n')
print(getCPUname())
print('\n\n')
print(getRAMinfo())
print('\n\n')
print(getDriveCapacity())
print('\n\n')
print(getDrivenames())
