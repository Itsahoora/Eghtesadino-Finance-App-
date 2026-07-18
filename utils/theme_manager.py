# Theme manager adapted for CustomTkinter (no Kivy dependency)
import os
import json
import customtkinter as ctk
from .theme.colors import DARK_COLORS


class ThemeManager:
    ANIMATION_DURATION = 0.28
    THEME_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'user_theme.json')

    def __init__(self):
        # default
        self.mode = 'dark'
        self._overrides = {}
        self._listeners = []
        # try loading saved preference
        self._load()
        # apply to CustomTkinter
        try:
            ctk.set_appearance_mode(self.mode.capitalize())
        except Exception:
            pass

    def _load(self):
        try:
            with open(self.THEME_FILE, 'r', encoding='utf-8') as fh:
                data = json.load(fh)
                self.mode = data.get('mode', self.mode)
        except FileNotFoundError:
            return
        except Exception:
            return

    def _save(self):
        try:
            with open(self.THEME_FILE, 'w', encoding='utf-8') as fh:
                json.dump({'mode': self.mode}, fh)
        except Exception:
            pass

    def toggle_mode(self):
        self.mode = 'light' if self.mode == 'dark' else 'dark'
        self._apply_mode()
        self._save()

    def set_mode(self, mode):
        if mode not in {'light', 'dark'}:
            return False
        self.mode = mode
        self._apply_mode()
        self._save()
        return True

    def reset(self):
        self.mode = 'dark'
        self._overrides = {}
        self._apply_mode()
        self._save()
        return True

    def _apply_mode(self):
        try:
            ctk.set_appearance_mode(self.mode.capitalize())
        except Exception:
            pass
        # notify listeners so UI can refresh colors
        for cb in list(self._listeners):
            try:
                cb()
            except Exception:
                pass

    # --- convenience API used by tests / settings UI ---
    def get_color(self, token, default=None):
        # return an override if present, otherwise look up base theme colors
        if token in self._overrides:
            return self._overrides[token]
        return DARK_COLORS.get(token, default)

    def set_color(self, token, value):
        self._overrides[token] = value
        for cb in list(self._listeners):
            try:
                cb()
            except Exception:
                pass

    def register_listener(self, cb):
        if cb not in self._listeners:
            self._listeners.append(cb)

    def unregister_listener(self, cb):
        try:
            self._listeners.remove(cb)
        except Exception:
            pass

    def apply_preset(self, name):
        # simple no-op preset applier; real presets could be added here
        return True

    def export_theme(self):
        # return a JSON-serializable snapshot
        data = {'mode': self.mode, 'overrides': self._overrides}
        return data

    def import_theme(self, data):
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception:
                return False
        if not isinstance(data, dict):
            return False
        self.mode = data.get('mode', self.mode)
        self._overrides = data.get('overrides', self._overrides)
        try:
            ctk.set_appearance_mode(self.mode.capitalize())
        except Exception:
            pass
        return True


# singleton instance used across the app
theme_manager = ThemeManager()