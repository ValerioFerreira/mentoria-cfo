from pathlib import Path
from playwright.sync_api import sync_playwright


def open_context(profile: Path, headless: bool, timeout_ms: int):
    """Start a persistent visible browser; passwords are entered only by the user."""
    profile.mkdir(parents=True, exist_ok=True)
    manager = sync_playwright().start()
    context = manager.chromium.launch_persistent_context(
        user_data_dir=str(profile.resolve()),
        headless=headless,
        accept_downloads=True,
        downloads_path=None,
        args=["--disable-blink-features=AutomationControlled"],
    )
    context.set_default_timeout(timeout_ms)
    return manager, context

