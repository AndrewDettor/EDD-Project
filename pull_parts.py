import subprocess


class PullParts():
    def getGPUname(self):
        get_gpu_info = "wmic path win32_VideoController get name"
        return subprocess.call(get_gpu_info, shell=True)

    def getCPUname(self):
        get_cpu_info = "wmic cpu get name"
        return subprocess.call(get_cpu_info, shell=True)

    def getRAMinfo(self):
        get_RAM_info = "wmic MEMORYCHIP get BankLabel, DeviceLocator, MemoryType, TypeDetail, Capacity, Speed"
        return subprocess.call(get_RAM_info, shell=True)

    def getDriveCapacity(self):
        get_drive_capacity = "wmic logicaldisk get size,freespace,caption"
        return subprocess.call(get_drive_capacity, shell=True)

    def getDrivenames(self):
        get_drive_names = "wmic diskdrive get caption"
        return subprocess.call(get_drive_names, shell=True)


# test
pp = PullParts()
print(pp.getGPUname())
print('\n\n')
print(pp.getCPUname())
print('\n\n')
print(pp.getRAMinfo())
print('\n\n')
print(pp.getDriveCapacity())
print('\n\n')
print(pp.getDrivenames())
