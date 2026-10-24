from src.models import SupportTicket, Learner, Course, Assessment, Registration
from src.config import AppConfig
from src.patterns.ticket_factory import TicketFactory
from src.monitoring.bugzot import BugzotMonitor
from src.patterns.grading_strategies import GradingContext, GradeClassification


from src.services.registration_engine import RegistrationEngine


def run_demo():
    print("==============================================================================")
    print("             ENTERPRISE DOMAIN MODEL DEMONSTRATION                           ")
    print("==============================================================================")
    print("DOMAIN MODEL OUTPUT")
    print("------------------------------------------------------------------------------")
    learner = Learner("L001", "Thabo Mokoena", "thabo.m@vossie.net")
    course= Course("PY701", "Enterprise Python Development", capacity=30)
    print(f"Learner ID: {learner.learner_id}, Name: {learner.name}")
    print(f"Course ID: {course.course_id}, Name: {course.name}")

    reg = Registration("R001", learner, course)
    reg.complete_registration()
    print(f"{learner.name} registered for {course.name}\n\n")

    print("             SINGLETON PATTERN DEMONSTRATION                                  ")
    print("------------------------------------------------------------------------------")
    config1 = AppConfig()
    config2 = AppConfig()
    print(f"Config1 ID: {id(config1)}")
    print(f"Config2 ID: {id(config2)}")
    if id(config1) == id(config2):
        print("Singleton Successful: Same Instance")
    else:
        print("Singleton Failed: Different Instances")

    print("\n             FACTORY PATTERN DEMONSTRATION                                    ")
    print("------------------------------------------------------------------------------") 
    t1= TicketFactory.create_ticket("AcademicTicket", "T001", learner, "Requesting rewrite of assessment")
    t2= TicketFactory.create_ticket("TechnicalTicket", "T003", learner, "System error while submitting assessment")
    t3= TicketFactory.create_ticket("RegistrationTicket", "T002", learner, "Course registration issue")
    print(f"Created:  {t1.ticket_id}")
    print(f"Created:  {t2.ticket_id}")
    print(f"Created:  {t3.ticket_id}\n\n")

    print("              STRATEGY PATTERN DEMONSTRATION                                  ")
    print("------------------------------------------------------------------------------") 
    score_percentage = 82
    grading = GradingContext(GradeClassification())
    classification = grading.run_classification(score_percentage)
    print(f"Percentage Result: {score_percentage}")
    print(f"Classification Result: {classification}")

    print("==============================================================================")
    print("               REGISTRATION PROCESSING ENGINE                                 ")
    print("==============================================================================")
    engine = RegistrationEngine()
    demo_course = Course("PY701", "Enterprise Python Development", capacity=30)
    for i in range(1, 15):
        demo_learner = Learner(f"{i}", f"Learner {i}", f"learner{i}@vossie.net")
        registration = Registration(f"REG-{i:03d}", demo_learner, demo_course)
        engine.process_registration(registration)
        print(f"[SUCCESS] Learner {i} registered")
    print("\n REGISTRATION SUMMARY")
    print("------------------------------------------------------------------------------")
    print(f"Total Registrations: {engine.process_count}")
    monitor = BugzotMonitor()
    monitor.generate_performance_report()
if __name__== "__main__":
    run_demo()
    
    
