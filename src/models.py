from datetime import datetime
from typing import Dict, List


class Learner:

    def __init__(self, learner_id: str, name: str, email: str):

        if not name:
            raise ValueError("Name cannot be empty.")
        if not email:
            raise ValueError("Email cannot be empty.")
        self.learner_id: str = learner_id
        self.name: str = name
        self.email: str = email
        self.enrolled_courses: List['Course'] = []
    def __repr__(self) -> str:
        return f"<Learner {self.learner_id}: {self.name} ({self.email})>"

class Course:

    def __init__(self, course_id: str, name: str, capacity: int = None, capactiy: int = None):
        # Accept either the correctly-spelled `capacity` or the common misspelling
        # `capactiy` (backwards-compatible). Normalize and validate the value.
        if capacity is None and capactiy is not None:
            capacity = capactiy
        if capacity is None:
            raise ValueError("capacity must be provided")

        self.course_id: str = course_id
        self.name: str = name
        self.capacity: int = capacity
        self.registered_learners: List[Learner] = []

    def is_full(self) -> bool:
        return len(self.registered_learners) >= self.capacity

    def __repr__(self) -> str:
        return f"<Course {self.course_id}: {self.name} (Capacity: {self.capacity}))>"

class Registration:

    def __init__(self, registration_id: str, learner: Learner, course: Course):
        self.registration_id: str = registration_id
        self.learner: Learner = learner
        self.course: Course = course
        self.registration_date: datetime = datetime.now()
        self.status: str = "PENDING"

    def complete_registration(self):
        self.status = "SUCCESS"
        self.course.registered_learners.append(self.learner)
        self.learner.enrolled_courses.append(self.course)

    def failed_registration(self):
        self.status = "FAILED"

class Assessment:

    def __init__(self, assessment_id: str, course: Course, title: str, max_marks: float):
        self.assessment_id: str = assessment_id
        self.course: Course = course
        self.title: str = title
        self.max_marks: float = max_marks
        self.scores: dict = {}# learner_id -> score

    def record_score(self, learner: Learner, score: float):
        if score < 0 or score > self.max_marks:
            raise ValueError(f"Score must be between 0 and {self.max_marks}.")
        if learner not in self.course.registered_learners:
            raise ValueError("Learner is not registered for this course.")
        self.scores[learner.learner_id] = score

class SupportTicket:

    def __init__(self, ticket_id: str, learner: Learner, issue: str):
        self.ticket_id: str = ticket_id
        self.learner: Learner = learner
        self.issue: str = issue
        self.status: str = "OPEN"

    def close_ticket(self):
        self.status = "RESOLVED"
    
