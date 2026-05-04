# ─── gestures.py ─────────────────────────────────────────────────────────────
# Hand gesture detection helpers using MediaPipe landmark indices.
#
# Landmark reference:
#   4  = Thumb tip       3  = Thumb IP
#   8  = Index tip       6  = Index PIP
#   12 = Middle tip      10 = Middle PIP
#   16 = Ring tip        14 = Ring PIP
#   20 = Pinky tip       18 = Pinky PIP


def fingers_up(lm) -> list[bool]:
    """
    Return a list of 5 bools: [thumb, index, middle, ring, pinky].
    True = finger is extended/up.
    """
    up = [lm[4].x < lm[3].x]          # thumb: compare x (mirrored frame)
    for tip, pip in zip([8, 12, 16, 20], [6, 10, 14, 18]):
        up.append(lm[tip].y < lm[pip].y)   # finger up = tip above PIP joint
    return up


def is_drawing(lm) -> bool:
    """One finger gesture: index up, middle down → drawing mode."""
    up = fingers_up(lm)
    return up[1] and not up[2]


def is_selecting(lm) -> bool:
    """Two finger gesture: index + middle both up → UI select mode."""
    up = fingers_up(lm)
    return up[1] and up[2]


def is_fist(lm) -> bool:
    """All fingers down → fist (can be used as clear gesture)."""
    up = fingers_up(lm)
    return not any(up[1:])


def is_open_hand(lm) -> bool:
    """All fingers up → open palm."""
    up = fingers_up(lm)
    return all(up[1:])
