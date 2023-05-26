from PowerStatistics import PowerManagement
from Database import PowerStatisticDatabase

import time
import matplotlib.pyplot as plt

def main():
    ps = PowerManagement()
    db = PowerStatisticDatabase("PowerStatistics", "statistics",1000)
    # start_statistic_timer(ps, db)
    draw_plot(ps)

def draw_plot(ps:PowerManagement):
    while True:
        data = ps.get_powerstatistic_object()

        # Extrahiere die Datenpunkte
        timestamps = data.timestamp
        cpu_percentages = data.cpu_percentage
        ram_used = data.ram_used
        ram_total = data.ram_used

        print(timestamps)

        # Erstelle den Plot
        plt.plot(timestamps, cpu_percentages, label="CPU")
        plt.plot(timestamps, ram_used, label="RAM Used")
        plt.plot(timestamps, ram_total, label="RAM Total")

        # Diagramm beschriften
        plt.xlabel("Zeit")
        plt.ylabel("Auslastung")
        plt.title("Systemauslastung")
        plt.legend()

        # Zeige den Plot an
        plt.show()
        time.sleep(1)
        

def start_statistic_timer(ps:PowerManagement, db:PowerStatisticDatabase):
    while True:
        db.insert_one_with_limit(ps.get_powerstatistic_object())
        time.sleep(1)
        print("\033c", end="")

if __name__ == "__main__":
    main()





