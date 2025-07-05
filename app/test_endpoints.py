import shutil
import time
from fastapi.testclient import TestClient
from app.main import app, BASE_DIR, UPLOAD_DIR

client = TestClient(app)


def test_home_view():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["Content-Type"]


def test_img_echo_view():
    img_saved_dir = BASE_DIR / "images"
    for path in img_saved_dir.glob("*"):
        response = client.post("/img-echo/", files={"file": open(path, "rb")})
        assert response.status_code == 200
        fext = str(path.suffix).replace(".", "")
        assert fext in response.headers["Content-Type"]

    # time.sleep(3)  # for testing directory creation
    shutil.rmtree(UPLOAD_DIR)
