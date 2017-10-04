import pytest

from etl import UploadJob

@pytest.fixture(scope="session")
def upload_job():
    return UploadJob("test.csv", "lon", "lat", "4326")

@pytest.fixture(scope="session")
def upload_job_no_geometry():
    return UploadJob("test.csv", "lon", "lat", "4326", "utf-8", True)

@pytest.fixture(scope="session")
def upload_job_wrong_geom():
    return UploadJob("test.csv", "wrong_lon", "wrong_lat", "4326")

@pytest.fixture(scope="session")
def record():
    return {
        "lon": "1",
        "lat": "2",
        "text_col": "a",
        "int_col": "1",
        "float_col": "1.0",
        "escape_col": "t'est",
        "wrong_lon": "181",
        "wrong_lat": "91",
        "unescapable": 1
    }