from app.settings import config


def test_endpoints_starts_with_base_path(test_app):
    for route in test_app.app.routes:
        if not route.path.startswith("/health"):
            assert route.path.startswith(config.BASE_PATH)