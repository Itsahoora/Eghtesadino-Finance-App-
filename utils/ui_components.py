"""Reusable themed UI components.

Provides ``Card``, ``TitleLabel``, ``ThemedLabel``, ``IconBadge``,
animated helpers, and a ``font()`` utility so every screen shares a
single, consistent look.
"""

import customtkinter as ctk
from utils.colors import COLORS
from utils.scale import sv
from utils.constants import FONT_FAMILY


# ── Font helper ──────────────────────────────────────────────────

def font(size_token=14, weight='normal'):
    """Return a (family, size, weight) tuple ready for widget ``font=``."""
    return (FONT_FAMILY, sv(size_token), weight)


# ── Basic components ─────────────────────────────────────────────

class Card(ctk.CTkFrame):
    """Rounded card container."""

    def __init__(self, radius=14, bg_color='card_bg', **kwargs):
        color = COLORS.get(bg_color, '#ffffff')
        super().__init__(**kwargs)
        try:
            self.configure(fg_color=color, corner_radius=sv(radius),
                           border_width=0)
        except Exception:
            self.configure(fg_color=color)


class TitleLabel(ctk.CTkLabel):
    """Large bold heading label."""

    def __init__(self, master=None, text='', size=20, **kwargs):
        super().__init__(master=master, text=text, font=font(size, 'bold'), **kwargs)


class SubtitleLabel(ctk.CTkLabel):
    """Medium-weight subtitle label."""

    def __init__(self, master=None, text='', size=14, **kwargs):
        super().__init__(master=master, text=text, font=font(size, 'bold'), **kwargs)


class BodyLabel(ctk.CTkLabel):
    """Regular body text label."""

    def __init__(self, master=None, text='', size=13, **kwargs):
        super().__init__(master=master, text=text, font=font(size), **kwargs)


class MutedLabel(ctk.CTkLabel):
    """Small muted / helper text."""

    def __init__(self, master=None, text='', size=11, **kwargs):
        kwargs.setdefault('text_color', COLORS.get('muted_text'))
        super().__init__(master=master, text=text, font=font(size), **kwargs)


class ThemedLabel(ctk.CTkLabel):
    """Label that reads its color from a token."""

    def __init__(self, master=None, text='', color_token='text', **kwargs):
        fg = COLORS.get(color_token, '#ffffff')
        super().__init__(master=master, text=text, text_color=fg, **kwargs)


class ThemedTextInput(ctk.CTkEntry):
    """Entry with themed background."""

    def __init__(self, bg_token='input_bg', **kwargs):
        bg = COLORS.get(bg_token, '#ffffff')
        super().__init__(**kwargs)
        try:
            self.configure(fg_color=bg, border_width=1,
                           border_color=COLORS.get('divider'))
        except Exception:
            pass


class IconBadge(ctk.CTkFrame):
    """Small circular badge with a Unicode icon."""

    def __init__(self, icon='', size=36, bg_color='primary', **kwargs):
        bg = COLORS.get(bg_color, '#3B82F6')
        s = sv(size)
        super().__init__(width=s, height=s, corner_radius=s // 2,
                         fg_color=bg, **kwargs)
        lbl = ctk.CTkLabel(self, text=icon,
                           font=font(int(s * 0.42)),
                           text_color=COLORS.get('text_on_primary'))
        lbl.place(relx=0.5, rely=0.5, anchor='center')


class ColorSwatch(ctk.CTkButton):
    """Circular color swatch button."""

    def __init__(self, color='#ffffff', size=36, **kwargs):
        s = sv(size)
        super().__init__(width=s, height=s, corner_radius=s // 2, **kwargs)
        try:
            self.configure(fg_color=COLORS.get(color, color))
        except Exception:
            self.configure(fg_color=color)


class PillButton(ctk.CTkButton):
    """Rounded pill-shaped button."""

    def __init__(self, text='', variant='primary', **kwargs):
        color = COLORS.get(variant, '#3B82F6')
        hover = COLORS.get('primary_hover', '#1D4ED8')
        super().__init__(text=text, fg_color=color, hover_color=hover,
                         corner_radius=sv(20), font=font(13, 'bold'),
                         **kwargs)


class SectionHeader(ctk.CTkFrame):
    """Card-like section with a bold title line, used in settings etc."""

    def __init__(self, title='', icon='', master=None, **kwargs):
        super().__init__(master, fg_color='transparent', **kwargs)

        left = ctk.CTkFrame(self, fg_color='transparent')
        left.pack(side='left', fill='x', expand=True)

        if icon:
            ctk.CTkLabel(left, text=icon, font=font(16),
                         text_color=COLORS.get('primary')
                         ).pack(side='left', padx=(0, sv(6)))

        ctk.CTkLabel(left, text=title, font=font(15, 'bold'),
                     text_color=COLORS.get('text')
                     ).pack(side='left')


class ThemeToggleButton(ctk.CTkButton):
    """Toggle between dark / light mode."""

    def __init__(self, get_mode_callback, toggle_callback, **kwargs):
        self.get_mode = get_mode_callback
        self.toggle_cb = toggle_callback
        mode = self.get_mode()
        icon = '\u2600' if mode == 'light' else '\u263E'
        super().__init__(text=f' {icon} ', command=self._on_click,
                         width=sv(44), height=sv(34),
                         corner_radius=sv(10), **kwargs)

    def _on_click(self):
        self.toggle_cb()
        mode = self.get_mode()
        icon = '\u2600' if mode == 'light' else '\u263E'
        self.configure(text=f' {icon} ')


# ── Animations ───────────────────────────────────────────────────

def animate_pulse(widget, attr='fg_color', color1=None, color2=None,
                  loops=2, delay=80):
    """Gently pulse a widget's attribute between two colors."""
    if widget is None:
        return

    try:
        original = widget.cget(attr)
    except Exception:
        original = None

    if color1 is None:
        color1 = COLORS.get('primary', '#3B82F6')
    if color2 is None:
        color2 = COLORS.get('card_bg', '#1E293B')

    sequence = []
    for _ in range(loops):
        sequence.append(color1)
        sequence.append(color2)
    if original is not None:
        sequence.append(original)

    def step(index):
        if index >= len(sequence):
            return
        try:
            widget.configure(**{attr: sequence[index]})
        except Exception:
            pass
        if index + 1 < len(sequence):
            widget.after(delay, step, index + 1)

    step(0)


def animate_card_intro(card):
    """Smooth fade-in pulse when a card first appears."""
    animate_pulse(card, attr='fg_color', loops=1, delay=90)


def animate_slide_in(widget, direction='left', distance=30, steps=8, delay=25):
    """Slide a widget into position from off-screen."""
    if widget is None:
        return

    try:
        pad_args = widget.pack_info().get('padx', 0)
        if isinstance(pad_args, (int, float)):
            start_x = -distance if direction == 'left' else distance
        else:
            start_x = 0
    except Exception:
        start_x = 0

    if start_x == 0:
        return

    delta = abs(start_x) // steps
    current = [start_x]

    def step():
        current[0] += delta if start_x < 0 else -delta
        if (start_x < 0 and current[0] >= 0) or (start_x > 0 and current[0] <= 0):
            return
        try:
            widget.pack_configure(padx=(current[0], 0))
        except Exception:
            pass
        widget.after(delay, step)

    step()
