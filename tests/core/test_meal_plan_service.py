from unittest import mock

from meal_plan.core.meal_plan_repository import MealPlanRepository
from meal_plan.core.meal_plan_service import MealPlanService


def test_get_meal_plan():
    service = MealPlanService(meal_plan_repository=mock.Mock(spec=MealPlanRepository))
    assert service.get_plan() is not None
