from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from meal_plan.containers import Container
from meal_plan.core.meal_plan_service import MealPlanService

router = APIRouter()


@router.get("/")
@inject
async def root(
    meal_plan_service: MealPlanService = Depends(Provide[Container.meal_plan_service]),
) -> object:
    return meal_plan_service.get_plan()
