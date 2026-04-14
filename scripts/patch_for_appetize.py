#!/usr/bin/env python3
"""Patches WholesaleConnect Swift source files for Appetize.io simulator build."""
import os

def patch(path, old, new):
    if not os.path.exists(path):
        print("SKIP (not found): " + path)
        return
    with open(path) as f:
        c = f.read()
    if old not in c:
        print("SKIP (already patched): " + path)
        return
    with open(path, 'w') as f:
        f.write(c.replace(old, new))
    print("OK: " + path)

# Fix GhostButtonStyle - add tint parameter
patch(
    'Shared/Theme/ButtonStyles.swift',
    'struct GhostButtonStyle: ButtonStyle {',
    'struct GhostButtonStyle: ButtonStyle {
    var tint: Color = .accent'
)
patch(
    'Shared/Theme/ButtonStyles.swift',
    '.foregroundColor(.accent)',
    '.foregroundColor(tint)'
)

print("All patches applied")
