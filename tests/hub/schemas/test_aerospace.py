from vlmrun.hub.schemas.aerospace.remote_sensing import (
    RemoteSensing,
    RemoteSensingCategory,
)


def test_remote_sensing_schema():
    # Test valid data
    data = {
        "description": "A satellite image showing an airport with multiple runways and terminals.",
        "objects": ["runway", "terminal", "aircraft", "parking lot"],
        "categories": ["airport", "runway", "commercial_area"],
    }
    rs = RemoteSensing(**data)
    assert rs.description == data["description"]
    assert rs.objects == data["objects"]
    assert all(isinstance(cat, RemoteSensingCategory) for cat in rs.categories)
