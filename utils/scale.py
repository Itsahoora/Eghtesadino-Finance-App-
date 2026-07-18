"""DPI-aware scaling utilities.

Caches the scale factor in memory so ``sv()`` never hits disk after
initial load.  Call ``init_scaling(app)`` once at startup.
"""

import os
import json
import customtkinter as ctk

_SCALE_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'user_scale.json')

_cached_scale: float | None = None


def _read_scale() -> float:
    try:
        with open(_SCALE_FILE, 'r') as f:
            return float(json.load(f).get('scale', 1.0))
    except Exception:
        return 1.0


def _write_scale(value: float) -> None:
    try:
        with open(_SCALE_FILE, 'w') as f:
            json.dump({'scale': value}, f)
    except Exception:
        pass


def init_scaling(app) -> None:
    """Calculate and apply the optimal scale factor for the current display."""
    global _cached_scale
    try:
        root = app.winfo_toplevel()
        screen_w = root.winfo_screenwidth()
        screen_h = root.winfo_screenheight()
    except Exception:
        screen_w, screen_h = 1366, 768

    scale = min(screen_w / 1366, screen_h / 768)
    scale = max(0.7, min(1.4, scale))

    _cached_scale = scale
    _write_scale(scale)

    for setter in (ctk.set_widget_scaling, ctk.set_window_scaling):
        try:
            setter(scale)
        except Exception:
            pass


def sv(value: float) -> int:
    """Scale a pixel value by the current DPI scale factor."""
    global _cached_scale
    if _cached_scale is None:
        _cached_scale = _read_scale()
    return int(value * _cached_scale)
