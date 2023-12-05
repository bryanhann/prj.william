#!/usr/bin/env python3
from vendor.rene import Colors
def red(txt):
    return f"{Colors.LIGHT_RED}{txt}{Colors.END}"
def green(txt):
    return f"{Colors.LIGHT_GREEN}{txt}{Colors.END}"
def ul(txt):
    return f"{Colors.UNDERLINE}{txt}{Colors.END}"

