import time
from datetime import datetime
from typing import Any, Dict, List, Optional
from src.models import Learner, Course, Assessment, Registration

class BugzotMonitor:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(BugzotMonitor, cls).__new__(cls)
            cls.instance._init_subsystem()
        return cls.instance

    def _init_subsystem(self):

        self.logs: List[Dict[str, Any]] = []
        self.start_time: float = time.time()
        self.transaction_durations: List[float] = []
        self.counts: Dict[str, int] = {
            "SUCCESS": 0,
            "VALIDATION_FAILURE": 0,
            "DUPLICATE_REGISTRATION": 0,
            "COURSE_FULL": 0,
            "ERROR": 0
        }

    def log_event(self, event_type: str, message: str, details: Optional[Dict[str, Any]] = None):
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "event_type": event_type,
            "message": message,
            "details": details or {}
        }
        self.logs.append(log_entry)

        if "SUCCESS" in event_type:
            self.counts["SUCCESS"] += 1
        elif "VALIDATION_FAILURE" in event_type:
            self.counts["VALIDATION_FAILURE"] += 1
        elif "DUPLICATE_REGISTRATION" in event_type:
            self.counts["DUPLICATE_REGISTRATION"] += 1
        elif "COURSE_FULL" in event_type:
            self.counts["COURSE_FULL"] += 1
        elif "ERROR" in event_type:
            self.counts["ERROR"] += 1

    def track_transaction_speed(self, duration: float):
        self.transaction_durations.append(duration)

    def print_event_log(self):
        print("\n ===================================================================")
        print("             BUGZOT MONITORING EVENT LOG                              ")
        print(" ===================================================================")
        for log in self.logs:
            print(f"[{log['timestamp']}] {log['event_type']}: {log['message']} - Details: {log['details']}")

    def generate_performance_report(self):
        total_transactions = len(self.transaction_durations)
        average_duration = sum(self.transaction_durations) / total_transactions if total_transactions > 0 else 0
        print("\n ===================================================================")
        print("             BUGZOT MONITORING PERFORMANCE REPORT                    ")
        print(" ===================================================================")
        print(f"Total Runtime: {time.time() - self.start_time:.2f} seconds")
        print(f"Total Transactions Processed: {total_transactions}")
        print(f"Average Transaction Duration: {average_duration:.4f} seconds")
        print(f"Successful Registrations: {self.counts['SUCCESS']}")
        print(f"Validation Failures: {self.counts['VALIDATION_FAILURE']}")
        print(f"Duplicate Registrations: {self.counts['DUPLICATE_REGISTRATION']}")
        print(f"Average Latency: {average_duration:.4f} seconds")

        return {
            "total_runtime": time.time() - self.start_time,
            "average_latency": average_duration,
            "metrics": self.counts
        }
    