import json
import sys
from PowerStatistics import PowerManagement
from Database import PowerStatisticDatabase
from PowerStatistics import StatisticObject

import time
import matplotlib.pyplot as plt

def main():
    ps = PowerManagement()
    db = PowerStatisticDatabase("PowerStatistics", "statistics",10)
    start_statistic_timer(ps, db)

# this def gets all statistics from the database and saves them in a list
def get_statistics_from_db(ps:PowerManagement, db:PowerStatisticDatabase):
    all_documents = db.find_all_documents_as_list()

    statistic_object_list = []

    for document in all_documents:
        timestamp = document.get("timestamp")
        cpu_percentage = document.get("cpu_percentage")
        ram_used = document.get("ram_used")
        ram_total = document.get("ram_total")

        statistic_object = StatisticObject(timestamp, cpu_percentage, ram_used, ram_total)
        statistic_object_list.append(statistic_object)

    plot_statistics(statistic_object_list)

# this def plots the statistics from the list
def plot_statistics(statistic_object_list: StatisticObject):
    x = []
    y = []

    statistic_object_list[:10]
    for statistic_object in statistic_object_list:
        x.append(statistic_object.timestamp)
        y.append(statistic_object.cpu_percentage)

    last_ram_used = statistic_object_list[-1].ram_used
    last_ram_total = statistic_object_list[-1].ram_total

    # Erstelle die Legende mit den letzten Werten
  



    plt.clf()
    plt.plot(x, y)
    plt.xticks(x, rotation='vertical')
    plt.xlabel('Timestamp')
    plt.ylabel('RAM Auslastung (%)')
    plt.legend(["RAM used: " + str(last_ram_used) + " MB, RAM total: " + str(last_ram_total) + " MB"],loc='upper left')
    plt.draw()
    plt.pause(0.001)



    if not plt.get_fignums():
        plt.close()
        print("Programm beendet")
        sys.exit()



def start_statistic_timer(ps:PowerManagement, db:PowerStatisticDatabase):
    i = 0
    while True:
        if i == 1:
            get_statistics_from_db(ps, db)
            i = 0
            print("Draw new plot")
        
        print("Insert new document")
        power_statistics = ps.get_powerstatistic_object()
        json_document = power_statistics.to_dict()
        db.insert_one_with_limit(json_document)
        time.sleep(1)
        print("\033c", end="")
        i += 1

if __name__ == "__main__":
    main()





