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

# Lint all files
lint:
    poetry run ruff check .

# Autoformatting
format:
    poetry run black .

# Run all code checks
check: typecheck lint
    poetry run black . --check

# Run all tests
test:
    poetry run pytest . -q
