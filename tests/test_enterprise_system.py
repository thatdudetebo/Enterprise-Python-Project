import unittest
import time
from src.models import Learner, Course, Registration
from src.config import AppConfig
from src.patterns.ticket_factory import TicketFactory
from src.patterns.grading_strategies import GradingContext, GradingStrategy, GradeClassification
from src.services.registration_engine import RegistrationEngine
from src.monitoring.bugzot import BugzotMonitor

class TestEnterpriseSystem(unittest.TestCase):

    def setUp(self):
        self.monitor = BugzotMonitor()
        self.monitor._init_subsystem()
        self.engine = RegistrationEngine()

    def learner_and_course_init(self):
        learner = Learner("L000","Jenny Doe", "jennyd@vossie.net")
        course = Course("PY101", "Introduction to Python", capacity=20)

        self.assertEqual(learner.learner_id, "L000")
        self.assertEqual(course.capacity, 20)
        self.assertFalse(course.is_full())

        with self.assertRaises(ValueError):
            Learner("","","null@vossie.net")

    def test_singleton_config_pattern(self):
        config1 = AppConfig()
        config2 = AppConfig()
        self.assertIs(config1, config2, "Singleton failed: Different addresss allocations!")

    def test_factory_ticket_creation(self):
        learner = Learner("L001", "Thabo", "thabo@vossie.net")
        ticket = TicketFactory.create_ticket("AcademicTicket", "T001", learner, "Exam access query")

        ticket_type = getattr(ticket, "type", getattr(ticket, "ticket_type", getattr(ticket, "category", None)))
        self.assertEqual(ticket_type, "AcademicTicket")
        self.assertEqual(ticket.status, "OPEN")

    def test_strategy_grading_classification(self):
        """Verifies dynamic business strategy results calculate boundaries flawlessly."""
        context = GradingContext(GradeClassification())
        
        self.assertEqual(context.run_classification(85.0), "Distinction")
        self.assertEqual(context.run_classification(60.0), "Pass")
        self.assertEqual(context.run_classification(40.0), "Fail")

    
    def test_concurrent_registration_processing(self):
        """Dispatches dynamic payloads to verify multi-threaded validation and capacity guards."""
        course = Course("PY-TH", "Advanced Threading", capacity=2)
        
        # 1. Valid requests filling slots completely
        lrnr1 = Learner("ST-1", "Student 1", "s1@vossie.net")
        lrnr2 = Learner("ST-2", "Student 2", "s2@vossie.net")
        reg1 = Registration("R-01", lrnr1, course)
        reg2 = Registration("R-02", lrnr2, course)
        
        # 2. Capacity overload query violation
        lrnr3 = Learner("ST-3", "Student 3", "s3@vossie.net")
        reg3 = Registration("R-03", lrnr3, course)
        
        # Dispatch parallel execution list block
        batch_results = self.engine.process_concurrent_batch([reg1, reg2, reg3])
        
        self.assertEqual(batch_results["successful_registrations"], 2)
        self.assertEqual(batch_results["failed_registrations"], 1)
        self.assertTrue(course.is_full())

    def test_bugzot_metric_aggregation(self):
        """Verifies data logs increments match engine execution event dispatches cleanly."""
        self.monitor.log_event("SUCCESS", "Registration executed successfully")
        self.monitor.log_event("COURSE_FULL", "Capacity bound breached constraint")
        
        report = self.monitor.generate_performance_report()
        self.assertEqual(report["metrics"]["SUCCESS"], 1)
        self.assertEqual(report["metrics"]["COURSE_FULL"], 1)
