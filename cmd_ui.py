from api import api
import os


def ui_percent(percent):
    for i in range(20):
        if percent > 5:
            print("#", end="")
        elif percent > 0:
            print("=", end="")
        else:
            print("-", end="")
        percent -= 5


@api.connect
def slot(arg):
    os.system('cls' if os.name == 'nt' else 'clear')

    used = arg['used_memory']
    total = arg['total_memory']
    percent = float(used*100/total)
    ui_percent(percent)
    print(" Использовано памяти {0} из {1} ({2}%)".format(used, total, percent))

    percent = float(arg['cpu_usage'])
    ui_percent(percent)
    print(" Процессор занят на {0}%".format(percent))

    percent = float(arg['ssd_usage'])
    ui_percent(percent)
    print(" ssd занят на {0}%".format(percent))
