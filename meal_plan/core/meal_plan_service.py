from .meal_plan import MealPlan
from .meal_plan_repository import MealPlanRepository


class MealPlanService:
    def __init__(self, meal_plan_repository: MealPlanRepository):
        self.meal_plan_repository = meal_plan_repository

    def get_plan(self) -> MealPlan:
        # TODO: Get the plan for the next 7 days by default
        return self.meal_plan_repository.get()
