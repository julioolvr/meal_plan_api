from abc import ABC, abstractmethod

from .meal_plan import MealPlan


class MealPlanRepository(ABC):
    @abstractmethod
    def get(self) -> MealPlan:
        raise NotImplementedError
