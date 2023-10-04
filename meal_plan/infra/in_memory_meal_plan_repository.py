from meal_plan.core.meal_plan import MealPlan
from meal_plan.core.meal_plan_repository import MealPlanRepository


class InMemoryMealPlanRepository(MealPlanRepository):
    def get(self) -> MealPlan:
        return MealPlan("TEST")
