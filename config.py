"""Defaults for the local, authenticated course PDF downloader."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    delay_between_pages: float = 1.0
    max_retries: int = 3
    timeout_ms: int = 30_000
    headless: bool = False
    profile_dir: str = "browser-profile"

