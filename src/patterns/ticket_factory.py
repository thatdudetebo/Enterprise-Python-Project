from src.models import SupportTicket, Learner

class AcademicTicket(SupportTicket):
    def __init__(self, ticket_id: str, learner: Learner, issue: str):
        super().__init__(ticket_id, learner, issue)
        self.category = "AcademicTicket"

class RegistrationTicket(SupportTicket):
    def __init__(self, ticket_id: str, learner: Learner, issue: str):
        super().__init__(ticket_id, learner, issue)
        self.category = "RegistrationTicket"

class TechnicalTicket(SupportTicket):
    def __init__(self, ticket_id: str, learner: Learner, issue: str):
        super().__init__(ticket_id, learner, issue)
        self.category = "TechnicalTicket"

class TicketFactory:
    @staticmethod
    def create_ticket(ticket_type: str, ticket_id: str, learner: Learner, issue: str) -> SupportTicket:
        normalized_type = (ticket_type or "").strip()
        lookup = {
            "AcademicTicket": AcademicTicket,
            "academic": AcademicTicket,
            "academic_ticket": AcademicTicket,
            "RegistrationTicket": RegistrationTicket,
            "registration": RegistrationTicket,
            "registration_ticket": RegistrationTicket,
            "TechnicalTicket": TechnicalTicket,
            "technical": TechnicalTicket,
            "technical_ticket": TechnicalTicket,
        }

        ticket_class = lookup.get(normalized_type)
        if ticket_class is None:
            supported = ", ".join(sorted({key for key in lookup if "_" in key or key.endswith("Ticket")}))
            raise ValueError(
                f"Unknown ticket type: {ticket_type}. Supported types are: {supported}"
            )

        return ticket_class(ticket_id, learner, issue)
    