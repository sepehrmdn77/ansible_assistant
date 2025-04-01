import pytest
import flet as ft
import sys
from pathlib import Path

# Add the 'src' directory to the Python path
src_path = str(Path(__file__).resolve().parent.parent / 'src')
sys.path.insert(0, src_path)

import main  # Now imports main from the src directory

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