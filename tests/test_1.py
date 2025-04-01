import main
from unittest.mock import Mock
import pytest
import flet as ft
import sys

sys.path.append('./src')  # working path


def test_app_initialization():
    conn = Mock()
    session_id = "test_session"
    loop = Mock()

    page = ft.Page(conn=conn, session_id=session_id, loop=loop)
    main.main(page)
    assert len(page.controls) > 0


@pytest.mark.parametrize("label_text", ["Start", "Stop", "Reset"])
def test_button_labels(label_text):
    conn = Mock()
    session_id = "test_session"
    loop = Mock()

    page = ft.Page(conn=conn, session_id=session_id, loop=loop)
    main.main(page)
    assert any(
        control for control in page.controls if control.label == label_text
    ), f"No control found with label '{label_text}'"
