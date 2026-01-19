import psutil
import datetime
import csv
import os

def generate_report():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    report = (
        "SYSTEM HEALTH CHECK REPORT\n"
        f"Timestamp     : {now}\n\n"
        f"CPU Usage     : {cpu} %\n"
        f"Memory Usage  : {memory} %\n"
        f"Disk Usage    : {disk} %\n"
        "-----------------------------\n\n"
    )

    return report
def save_report_csv(cpu, memory, disk):
    filename = "system_health_report.csv"
    file_exists = os.path.isfile(filename)

    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Timestamp", "CPU %", "Memory %", "Disk %"])

        writer.writerow([
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            cpu,
            memory,
            disk
        ])

if __name__ == "__main__":
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print("System Health Check Completed")
    save_report_csv(cpu, memory, disk)

