import pandas as pd
from datetime import datetime

class AttendanceLogger:
    def log(self, name, filename="attendance/attendance.csv"):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df = pd.DataFrame([[name, time]], columns=["Name", "Timestamp"])

        try:
            existing = pd.read_csv(filename)
            df = pd.concat([existing, df], ignore_index=True)
        except FileNotFoundError:
            pass

        df.to_csv(filename, index=False)