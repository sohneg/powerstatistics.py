from PowerStatistics import PowerManagment
from Database import PowerStatisticDatabase

import time
import matplotlib.pyplot as plt

def main():
    ps = PowerManagment()
    db = PowerStatisticDatabase("PowerStatistics", "statistics",1000)
    # start_statistic_timer(ps, db)
    data = ps.get_all_powerstatistics_json()

    # Extrahiere die Datenpunkte
    timestamps = data["timestamp"]
    cpu_percentages = data["cpu"]
    ram_used = data["ram_used"]
    ram_total = data["ram_total"]

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
    
def start_statistic_timer(ps:PowerManagment, db:PowerStatisticDatabase):
    while True:
        db.insert_one_with_limit(ps.get_all_powerstatistics_json())
        time.sleep(1)
        print("\033c", end="")

if __name__ == "__main__":
    main()





