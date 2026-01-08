import pytest
from dash.testing.application_runners import import_app

@pytest.fixture
def app():
    return import_app("app")

def test_header_present(dash_duo, app):
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Pink Morsel Sales" in header.text

def test_graph_present(dash_duo, app):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None


def test_region_picker_present(dash_duo, app):
    dash_duo.start_server(app)

    radio_items = dash_duo.find_element("#region-filter")
    assert radio_items is not None

