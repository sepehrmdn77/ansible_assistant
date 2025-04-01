import pytest
import flet as ft
import sys
import asyncio
from pathlib import Path

# Add the 'src' directory to Python path
src_path = str(Path(__file__).resolve().parent.parent / 'src')
sys.path.insert(0, src_path)

import main

# Enable async test execution
@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

# Test initialization
async def test_app_initialization(page):
    await main.main(page)  # Wait for app initialization
    assert len(page.controls) > 0  # Verify controls are loaded

# Parameterized button test
@pytest.mark.parametrize("label_text", ["Start", "Stop", "Reset"])
async def test_button_labels(page, label_text):
    await main.main(page)
    assert any(
        control.label == label_text for control in page.controls
    ), f"Missing button: {label_text}"