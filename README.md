System Health Check Automation

Overview

This project automates system health monitoring by collecting key performance metrics such as CPU usage, memory utilization, and disk usage. The script generates timestamped reports that help track system performance trends over time.

Features

- Monitors CPU, memory, and disk usage
- Generates reports in CSV format
- Timestamped data for historical analysis
- Simple and lightweight Python automation
- Can be scheduled using cron or Task Scheduler

Tech Stack

- Python 3
- psutil library
- CSV for data storage

How to Run

1. Clone the repository
2. Install dependencies
   `python3 -m pip install -r requirements.txt`
3. Run the script
   `python3 system_health_check.py`

Sample Output

Sample CSV report is available in the `sample_output` folder.

Use Cases

- System diagnostics
- Performance monitoring
- Automation projects for DevOps / QA / SRE roles
