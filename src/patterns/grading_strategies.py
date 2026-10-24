from abc import ABC, abstractmethod
from src.models import Assessment, Learner


class GradingStrategy(ABC):

    @abstractmethod
    def calculate_grade(self, assessment: Assessment, learner: Learner) -> float:
        pass

    @abstractmethod
    def classify(self, percentage: float) -> str:
        pass


class GradeClassification(GradingStrategy):
    def calculate_grade(self, assessment: Assessment, learner: Learner) -> float:
        raise NotImplementedError

    def classify(self, percentage: float) -> str:
        if percentage >= 75:
            return "Distinction"
        elif percentage >= 50:
            return "Pass"
        else:
            return "Fail"


class GradingContext:
    def __init__(self, strategy: GradingStrategy):
        self._strategy = strategy

    def run_classification(self, percentage: float) -> str:
        return self._strategy.classify(percentage)

