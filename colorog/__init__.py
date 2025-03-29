from colorama import just_fix_windows_console
from termcolor import colored, cprint
from affixr import checked
from datetime import datetime
from sys import exc_info
import sys

# use Colorama to make Termcolor work on Windows too
just_fix_windows_console()


def get_frame_fallback(n):
    try:
        raise Exception
    except Exception:
        frame = exc_info()[2].tb_frame.f_back
        for _ in range(n):
            frame = frame.f_back
        return frame


def load_get_frame_function():
    if hasattr(sys, "_getframe"):
        get_frame = sys._getframe
    else:
        get_frame = get_frame_fallback
    return get_frame


get_frame = load_get_frame_function()


def get_frame_str():
    try:
        frame = get_frame(3)
    except ValueError:
        f_globals = {}
        f_lineno = 0
        co_name = "<unknown>"
    else:
        f_globals = frame.f_globals
        f_lineno = frame.f_lineno
        co_name = frame.f_code.co_name

    try:
        name = f_globals["__name__"]
        f_name = checked(co_name, 255)
    except KeyError:
        name = None

    return "%s:%s:%s" % (
        colored(name, "cyan"),
        colored(co_name, "cyan"),
        colored(f_lineno, "cyan"),
    )


def _time():
    return datetime.utcnow().isoformat(" ")[:-3]


LEVEL_PADDING = 8


def _log(message: str, level: str, color: str):
    time_str = colored(_time(), "cyan")
    level_str = colored(level.ljust(LEVEL_PADDING, " "), color)
    frame_str = get_frame_str()
    message_str = colored(message, color)
    print("%s | %s | %s - %s" % (time_str, level_str, frame_str, message_str))


def log_trace(message: str):
    _log(message, "TRACE", "blue")


def log_debug(message: str):
    _log(message, "DEBUG", "light_grey")


def log_info(message: str):
    _log(message, "INFO", "grey")


def log_success(message: str):
    _log(message, "SUCCESS", "green")


def log_warning(message: str):
    _log(message, "WARNING", "yellow")


def log_error(message: str):
    _log(message, "ERROR", "red")


def log_critical(message: str):
    _log(message, "CRITICAL", "light_red")


if __name__ == "__main__":
    print("")
    log_trace("This is trace")
    log_debug("This is debug")
    log_info("This is info")
    log_success("This is success")
    log_warning("This is warning")
    log_error("This is error")
    log_critical("This is critical")
    print("")
