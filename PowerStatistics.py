#!/usr/bin/python3

import time
import psutil

class PowerManagment:
    """
    return cpu usage in percent
    """
    def get_cpu_percentage(self):
        return psutil.cpu_percent()

    # return ram total in MB
    def get_ram_total(self):
        return round(psutil.virtual_memory().total / 1024 / 1024, 2)

    # return ram used in MB
    def get_ram_used(self):
        return round(psutil.virtual_memory().used / 1024 / 1024,2)

    # return current timestamp
    def get_timestamp(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # return all values as json
    def get_all_powerstatistics_json(self):
        return {
            "cpu": self.get_cpu_percentage(),
            "ram_used": self.get_ram_used(),
            "ram_total": self.get_ram_total(),
            "timestamp": self.get_timestamp()
        }

    # return all values as string
    def get_all_powerstatistics_string(self):
        return "ram total: " + str(self.cpu()) + " MB,","ram total: "  + str(self.ram())+ " MB,", "ram used: " +str(self.ram_used())+ " MB,", str(self.timestamp())+" (UTC)"


# class StatisticObject:
    