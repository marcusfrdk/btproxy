#!/usr/bin/env python3

import evdev
import os
from datetime import datetime

scan_to_hid = {
    # Reserved: 0
    # ErrorRollOver: 1
    # POSTFail: 2
    # ErrorUndefined: 3

    evdev.ecodes.KEY_A: 0x04,
    evdev.ecodes.KEY_B: 0x05,
    evdev.ecodes.KEY_C: 0x06,
    evdev.ecodes.KEY_D: 0x07,
    evdev.ecodes.KEY_E: 0x08,
    evdev.ecodes.KEY_F: 0x09,
    evdev.ecodes.KEY_G: 0x0a,
    evdev.ecodes.KEY_H: 0x0b,
    evdev.ecodes.KEY_I: 0x0c,
    evdev.ecodes.KEY_J: 0x0d,
    evdev.ecodes.KEY_K: 0x0e,
    evdev.ecodes.KEY_L: 0x0f,
    evdev.ecodes.KEY_M: 0x10,
    evdev.ecodes.KEY_N: 0x11,
    evdev.ecodes.KEY_O: 0x12,
    evdev.ecodes.KEY_P: 0x13,
    evdev.ecodes.KEY_Q: 0x14,
    evdev.ecodes.KEY_R: 0x15,
    evdev.ecodes.KEY_S: 0x16,
    evdev.ecodes.KEY_T: 0x17,
    evdev.ecodes.KEY_U: 0x18,
    evdev.ecodes.KEY_V: 0x19,
    evdev.ecodes.KEY_W: 0x1a,
    evdev.ecodes.KEY_X: 0x1b,
    evdev.ecodes.KEY_Y: 0x1c,
    evdev.ecodes.KEY_Z: 0x1d,

    evdev.ecodes.KEY_1: 0x1e,
    evdev.ecodes.KEY_2: 0x1f,
    evdev.ecodes.KEY_3: 0x20,
    evdev.ecodes.KEY_4: 0x21,
    evdev.ecodes.KEY_5: 0x22,
    evdev.ecodes.KEY_6: 0x23,
    evdev.ecodes.KEY_7: 0x24,
    evdev.ecodes.KEY_8: 0x25,
    evdev.ecodes.KEY_9: 0x26,
    evdev.ecodes.KEY_0: 0x27,

    evdev.ecodes.KEY_ENTER: 0x28,
    evdev.ecodes.KEY_ESC: 0x29,
    evdev.ecodes.KEY_BACKSPACE: 0x2a,
    evdev.ecodes.KEY_TAB: 0x2b,
    evdev.ecodes.KEY_SPACE: 0x2c,

    evdev.ecodes.KEY_MINUS: 0x2d,
    evdev.ecodes.KEY_EQUAL: 0x2e,
    evdev.ecodes.KEY_LEFTBRACE: 0x2f,
    evdev.ecodes.KEY_RIGHTBRACE: 0x30,
    evdev.ecodes.KEY_BACKSLASH: 0x31,
    # Non-US # and ~: 0x32,
    evdev.ecodes.KEY_SEMICOLON: 0x33,
    evdev.ecodes.KEY_APOSTROPHE: 0x34,
    evdev.ecodes.KEY_GRAVE: 0x35,
    evdev.ecodes.KEY_COMMA: 0x36,
    evdev.ecodes.KEY_DOT: 0x37,
    evdev.ecodes.KEY_SLASH: 0x38,

    evdev.ecodes.KEY_CAPSLOCK: 0x39,

    evdev.ecodes.KEY_F1: 0x3a,
    evdev.ecodes.KEY_F2: 0x3b,
    evdev.ecodes.KEY_F3: 0x3c,
    evdev.ecodes.KEY_F4: 0x3d,
    evdev.ecodes.KEY_F5: 0x3e,
    evdev.ecodes.KEY_F6: 0x3f,
    evdev.ecodes.KEY_F7: 0x40,
    evdev.ecodes.KEY_F8: 0x41,
    evdev.ecodes.KEY_F9: 0x42,
    evdev.ecodes.KEY_F10: 0x43,
    evdev.ecodes.KEY_F11: 0x44,
    evdev.ecodes.KEY_F12: 0x45,

    evdev.ecodes.KEY_PRINT: 0x46,
    evdev.ecodes.KEY_SCROLLLOCK: 0x47,
    evdev.ecodes.KEY_PAUSE: 0x48,
    evdev.ecodes.KEY_INSERT: 0x49,
    evdev.ecodes.KEY_HOME: 0x4a,
    evdev.ecodes.KEY_PAGEUP: 0x4b,
    evdev.ecodes.KEY_DELETE: 0x4c,
    evdev.ecodes.KEY_END: 0x4d,
    evdev.ecodes.KEY_PAGEDOWN: 0x4e,

    evdev.ecodes.KEY_RIGHT: 0x4f,
    evdev.ecodes.KEY_LEFT: 0x50,
    evdev.ecodes.KEY_DOWN: 0x51,
    evdev.ecodes.KEY_UP: 0x52,
    evdev.ecodes.KEY_NUMLOCK: 0x53,
    evdev.ecodes.KEY_KPSLASH: 0x54,
    evdev.ecodes.KEY_KPASTERISK: 0x55,
    evdev.ecodes.KEY_KPMINUS: 0x56,
    evdev.ecodes.KEY_KPPLUS: 0x57,
    evdev.ecodes.KEY_KPENTER: 0x58,

    evdev.ecodes.KEY_KP1: 0x1e,
    evdev.ecodes.KEY_KP2: 0x1f,
    evdev.ecodes.KEY_KP3: 0x20,
    evdev.ecodes.KEY_KP4: 0x21,
    evdev.ecodes.KEY_KP5: 0x22,
    evdev.ecodes.KEY_KP6: 0x23,
    evdev.ecodes.KEY_KP7: 0x24,
    evdev.ecodes.KEY_KP8: 0x25,
    evdev.ecodes.KEY_KP9: 0x26,
    evdev.ecodes.KEY_KP0: 0x27 ,

    evdev.ecodes.KEY_KPDOT: 0x37,
    # non-us / and |: 0x64,
    evdev.ecodes.KEY_APPSELECT: 0x65,
    evdev.ecodes.KEY_POWER: 0x66,
    evdev.ecodes.KEY_KPEQUAL: 0x2e,

    evdev.ecodes.KEY_F13: 0x68,
    evdev.ecodes.KEY_F14: 0x69,
    evdev.ecodes.KEY_F15: 0x6a,
    evdev.ecodes.KEY_F16: 0x6b,
    evdev.ecodes.KEY_F17: 0x6c,
    evdev.ecodes.KEY_F18: 0x6d,
    evdev.ecodes.KEY_F19: 0x6e,
    evdev.ecodes.KEY_F20: 0x6f,
    evdev.ecodes.KEY_F21: 0x70,
    evdev.ecodes.KEY_F22: 0x71,
    evdev.ecodes.KEY_F23: 0x72,
    evdev.ecodes.KEY_F24: 0x73,

    # execute
    evdev.ecodes.KEY_HELP: 0x75,
    evdev.ecodes.KEY_MENU: 0x76,
    evdev.ecodes.KEY_SELECT: 0x77,
    evdev.ecodes.KEY_STOP: 0x78,
    evdev.ecodes.KEY_AGAIN: 0x79,
    evdev.ecodes.KEY_UNDO: 0x7a,
    evdev.ecodes.KEY_CUT: 0x7b,
    evdev.ecodes.KEY_COPY: 0x7c,
    evdev.ecodes.KEY_PASTE: 0x7d,
    evdev.ecodes.KEY_FIND: 0x7e,

    evdev.ecodes.KEY_MUTE: 0x7f,
    evdev.ecodes.KEY_VOLUMEUP: 0x80,
    evdev.ecodes.KEY_VOLUMEDOWN: 0x81,

    # locking caps
    # locking num
    # locking scroll

    # ...

    evdev.ecodes.KEY_SYSRQ: 0x9a,

    # ...
}


modifiers = {
    evdev.ecodes.KEY_LEFTCTRL: 1 << 0,
    evdev.ecodes.KEY_LEFTSHIFT: 1 << 1,
    evdev.ecodes.KEY_LEFTALT: 1 << 2,
    evdev.ecodes.KEY_LEFTMETA: 1 << 3,

    evdev.ecodes.KEY_RIGHTCTRL: 1 << 4,
    evdev.ecodes.KEY_RIGHTSHIFT: 1 << 5,
    evdev.ecodes.KEY_RIGHTALT: 1 << 6,
    evdev.ecodes.KEY_RIGHTMETA: 1 << 7,
}

def log(msg: str) -> None:
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = f"{dt} {msg}\n"
    with open("./bthid.log", "a", encoding="utf-8") as f:
        f.write(msg)
    print(msg, end="")


class Keyboard(object):
    def __init__(self, dst):
        self.modifier_state = 0
        self.keys_down = set()
        self.dst = dst

    def __call__(self, event):
        if event.type != evdev.ecodes.EV_KEY:
            return
        
        #print("Keyboard", event)

        data = evdev.categorize(event)

        modifier = modifiers.get(data.scancode, None)
        if modifier:
            if data.keystate == data.key_down:
                self.modifier_state |= modifier
            if data.keystate == data.key_up:
                self.modifier_state &= ~modifier
        else:
            code = scan_to_hid.get(data.scancode, None)
            if code is None:
                log("Ignoring unknown key", data)
                return

            if data.keystate == data.key_down:
                if len(self.keys_down) >= 6:
                    log("Ignoring key due to rollover")
                    return
                self.keys_down.add(code)

            if data.keystate == data.key_up:
                self.keys_down.remove(code)

        # Build the packet
        packet = [self.modifier_state, 0] + [k for k in self.keys_down]
        packet += [0] * (8 - len(packet))

        #print("Keyboard sending")

        assert(len(packet) == 8)
        os.write(self.dst, bytes(packet))


class Consumer(object):
    BITS = {
        evdev.ecodes.KEY_NEXTSONG: (1 << 0),
        evdev.ecodes.KEY_PREVIOUSSONG: (1 << 1),
        # STOP key: 2
        # EJECT key: 3
        evdev.ecodes.KEY_PLAYPAUSE: (1 << 4),
        evdev.ecodes.KEY_MUTE: (1 << 5),
        evdev.ecodes.KEY_MUTE: (1 << 5),
        evdev.ecodes.KEY_VOLUMEUP: (1 << 6),
        evdev.ecodes.KEY_VOLUMEDOWN: (1 << 7),
    }

    def __init__(self, dst):
        self.state = 0
        self.dst = dst

    def __call__(self, event):
        if event.type != evdev.ecodes.EV_KEY:
            return
        
        #print("Consumer", event)

        data = evdev.categorize(event)
        bit = self.BITS.get(data.scancode, None)
        if bit is None:
            return

        self.state ^= bit
        payload=bytes([self.state])
        os.write(self.dst, payload)

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Forward input events to a USB descriptor')
    # parser.add_argument('-i', '--input', type=str, action='append', help='A source evdev device')
    # parser.add_argument('-k', '--keyboard', type=str, help='The keyboard output HID device')
    # parser.add_argument('-m', '--mouse', type=str, help='The mouse output HID device')
    # parser.add_argument('-c', '--consumer', type=str, help='The consumer output HID device')

    # args = parser.parse_args()

    try:
        src = evdev.InputDevice('/dev/input/event1')
        kbd = Keyboard(os.open("/dev/hidg0", os.O_WRONLY))
        con = Consumer(os.open("/dev/hidg1", os.O_WRONLY))
        src.grab()

        while True:
            for event in src.read_loop():
                kbd(event)
                con(event)
                raise ValueError("Placeholder error")
    except KeyboardInterrupt:
        pass
    except Exception as e:
        log("Exception: " + str(e))
    finally:
        log("Exiting...")
        src.ungrab()
        kbd.dst.close()
        con.dst.close()

        
