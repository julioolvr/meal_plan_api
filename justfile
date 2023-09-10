default:
  just --list

# Setup the environment
setup:
    poetry install

alias tc := typecheck

# Typecheck the whole project
typecheck:
    poetry run mypy .

# Run the development environment
dev:
    poetry run uvicorn meal_plan.main:app --reload
