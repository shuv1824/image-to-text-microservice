import io
import shutil

# import time
from fastapi.testclient import TestClient
from app.main import app, BASE_DIR, UPLOAD_DIR, get_settings
from PIL import Image, ImageChops

client = TestClient(app)


def test_home_view():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["Content-Type"]


def test_prediction_view():
    settings = get_settings()
    img_saved_dir = BASE_DIR / "images"
    for path in img_saved_dir.glob("*"):
        try:
            img = Image.open(path)
        except:
            img = None

        response = client.post(
            "/",
            files={"file": open(path, "rb")},
            headers={"Authorization": f"Bearer {settings.app_auth_token}"},
        )

        if img is None:
            assert response.status_code == 400
        else:
            assert response.status_code == 200
            data = response.json()
            assert len(data.keys()) == 2


def test_img_echo_view():
    img_saved_dir = BASE_DIR / "images"
    for path in img_saved_dir.glob("*"):
        try:
            img = Image.open(path)
        except:
            img = None

        response = client.post("/img-echo/", files={"file": open(path, "rb")})

        if img is None:
            assert response.status_code == 400
        else:
            assert response.status_code == 200
            r_stream = io.BytesIO(response.content)
            r_img = Image.open(r_stream)
            assert ImageChops.difference(img, r_img).getbbox() is None

    # time.sleep(3)  # for testing directory creation
    shutil.rmtree(UPLOAD_DIR)
