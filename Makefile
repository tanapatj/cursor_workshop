.PHONY: check setup score test test-part1 test-part2 coverage coverage-part1 watch clean

# Install dependencies
setup:
	pip install -r requirements.txt

# Verify the setup is working
check:
	@echo "Checking Python version..."
	@python --version
	@echo "Checking dependencies..."
	@python -m pytest --version
	@echo ""
	@echo "Setup looks good! Run 'make score' to see the competition board."

# Show competition scoreboard (Part 2)
score:
	@python scripts/show_score.py

# Run all tests
test:
	@python -m pytest -v

# Run Part 1 tests only
test-part1:
	@python -m pytest part1_demo/tests/ -v

# Run Part 2 competition tests only
test-part2:
	@python -m pytest part2_competition/tests/ -v

# Full coverage report
coverage:
	@python -m pytest --cov=part1_demo --cov=part2_competition/src \
		--cov-report=term-missing --cov-report=html \
		-q 2>/dev/null || true
	@echo ""
	@echo "HTML report saved to htmlcov/index.html"

# Part 1 coverage only
coverage-part1:
	@python -m pytest part1_demo/tests/ \
		--cov=part1_demo \
		--cov-report=term-missing \
		-v

# Auto-refresh score when files change (requires pytest-watch)
watch:
	@echo "Watching for changes... (Ctrl+C to stop)"
	@ptw part2_competition/ -- python scripts/show_score.py

# Remove cache/build artifacts
clean:
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name ".coverage" -delete 2>/dev/null || true
	@echo "Cleaned!"
