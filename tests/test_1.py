import pytest
import flet as ft
import sys
sys.path.append('./src') 
import main

def test_app_initialization():
    page = ft.Page()
    main.main(page)
    assert len(page.controls) > 0

@pytest.mark.parametrize("label_text", ["Start", "Stop", "Reset"])
def test_button_labels(label_text):
    page = ft.Page()
    main.main(page)
    assert any(
        control for control in page.controls if control.label == label_text
    ), f"No control found with label '{label_text}'"
    