import pytest
from flet import Page
import main

def test_app_initialization():
    page = Page()
    main.main(page)
    assert len(page.controls) > 0

@pytest.mark.parametrize("label_text", ["Start", "Stop", "Reset"])
def test_button_labels(label_text):
    page = Page()
    main.main(page)
    assert any(
        control for control in page.controls if control.label == label_text
    ), f"No control found with label '{label_text}'"
    