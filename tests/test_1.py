import pytest
import flet as ft
import sys

sys.path.append('./src')

from src import main

def test_app_initialization():
    conn = None
    session_id = "test_session"
    loop = None

    page = ft.Page(conn=conn, session_id=session_id, loop=loop)
    main.main(page)
    assert len(page.controls) > 0

@pytest.mark.parametrize("label_text", ["Start", "Stop", "Reset"])
def test_button_labels(label_text):
    conn = None
    session_id = "test_session"
    loop = None

    page = ft.Page(conn=conn, session_id=session_id, loop=loop)
    main.main(page)
    assert any(
        control for control in page.controls if control.label == label_text
    ), f"No control found with label '{label_text}'"
