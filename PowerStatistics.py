import time
import psutil

class PowerManagement:
    """
    Return CPU usage in percent.
    """
    def get_cpu_percentage(self):
        return psutil.cpu_percent()

    # Return RAM total in MB.
    def get_ram_total(self):
        return round(psutil.virtual_memory().total / 1024 / 1024, 2)

    # Return RAM used in MB.
    def get_ram_used(self):
        return round(psutil.virtual_memory().used / 1024 / 1024, 2)

    # Return current timestamp.
    def get_timestamp(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # Return all values as a StatisticObject instance.
    def get_powerstatistic_object(self):
        return StatisticObject(
            self.get_timestamp(),
            self.get_cpu_percentage(),
            self.get_ram_used(),
            self.get_ram_total()
        )

    # Return all values as a string.
    def get_all_powerstatistics_string(self):
        return (
            "RAM total: " + str(self.get_ram_total()) + " MB,",
            "RAM used: " + str(self.get_ram_used()) + " MB,",
            str(self.get_timestamp()) + " (UTC)"
        )


class StatisticObject:
    def __init__(self, timestamp, cpu_percentage, ram_used, ram_total):
        self.timestamp = timestamp
        self.cpu_percentage = cpu_percentage
        self.ram_used = ram_used
        self.ram_total = ram_total
