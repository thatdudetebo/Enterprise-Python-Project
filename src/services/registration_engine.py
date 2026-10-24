import threading
import time
from typing import List, Dict, Any
from src.models import Learner, Course, Assessment, Registration
from src.monitoring.bugzot import BugzotMonitor

class RegistrationEngine:

    def __init__(self):

        self.lock = threading.Lock()
        self.process_count = 0
        self.successful_registrations: List[Registration] = []
        self.failed_registrations: List[Registration] = []

    def process_registration(self, registration: Registration):
        monitor = BugzotMonitor()
        start_time = time.time()

        with self.lock:
            self.process_count += 1

            if not registration.learner.learner_id or not registration.course:
                registration.failed_registration()
                self.failed_registrations.append(registration)
                monitor.log_event("VALIDATION_FAILURE", "Validation failed for registration", {
                    "registration_id": registration.registration_id,
                    "learner_id": registration.learner.learner_id,
                    "course_id": registration.course.course_id if registration.course else None
                })
                monitor.track_transaction_speed(time.time() - start_time)
                return registration

            if any(existing_registration.learner.learner_id == registration.learner.learner_id and
                   existing_registration.course.course_id == registration.course.course_id
                   for existing_registration in self.successful_registrations):
                registration.failed_registration()
                self.failed_registrations.append(registration)
                monitor.log_event("DUPLICATE_REGISTRATION", "Duplicate registration attempt", {
                    "registration_id": registration.registration_id,
                    "learner_id": registration.learner.learner_id,
                    "course_id": registration.course.course_id if registration.course else None
                })
                monitor.track_transaction_speed(time.time() - start_time)
                return registration

            if any(existing_registration.learner.learner_id == registration.learner.learner_id and
                   existing_registration.course.course_id == registration.course.course_id
                   for existing_registration in self.successful_registrations):
                registration.failed_registration()
                self.failed_registrations.append(registration)
                monitor.log_event("DUPLICATE_REGISTRATION", "Duplicate registration attempt", {
                    "registration_id": registration.registration_id,
                    "learner_id": registration.learner.learner_id,
                    "course_id": registration.course.course_id
                })
                monitor.track_transaction_speed(time.time() - start_time)
                return registration

            if registration.course.is_full():
                registration.failed_registration()
                self.failed_registrations.append(registration)
                monitor.log_event("COURSE_FULL", "Course is full", {
                    "registration_id": registration.registration_id,
                    "learner_id": registration.learner.learner_id,
                    "course_id": registration.course.course_id
                })
                monitor.track_transaction_speed(time.time() - start_time)
                return registration
            
            time.sleep(0.1)
            registration.complete_registration()
            self.successful_registrations.append(registration)

            monitor.log_event("SUCCESS", f"{registration.learner.name} registration successful")
            monitor.track_transaction_speed(time.time() - start_time)
            return registration
    def process_concurrent_batch(self, requests: List[Registration]) -> Dict[str, Any]:
        threads = []
        results = []

        def worker(registration: Registration):
            result = self.process_registration(registration)
            results.append(result)

        for request in requests:
            thread = threading.Thread(target=worker, args=(request,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return {
            "total_requests": len(requests),
            "successful_registrations": len(self.successful_registrations),
            "failed_registrations": len(self.failed_registrations),
            "results": results
        }
    def engine_summary(self):
        total_registrations = len(self.successful_registrations) + len(self.failed_registrations)
        return total_registrations
    
