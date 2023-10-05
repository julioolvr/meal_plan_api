from dependency_injector import containers, providers

from meal_plan.core.meal_plan_service import MealPlanService
from meal_plan.infra.in_memory_meal_plan_repository import InMemoryMealPlanRepository


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".api.endpoints"])

    meal_plan_repository = providers.Factory(InMemoryMealPlanRepository)

    meal_plan_service = providers.Factory(
        MealPlanService, meal_plan_repository=meal_plan_repository
    )
