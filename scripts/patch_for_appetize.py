#!/usr/bin/env python3
import os

NL = chr(10)

def patch(path, old, new):
    if not os.path.exists(path):
        print('SKIP (not found): ' + path)
        return
    with open(path) as f:
        c = f.read()
    if old not in c:
        print('SKIP (already patched): ' + path)
        return
    with open(path, 'w') as f:
        f.write(c.replace(old, new))
    print('OK: ' + path)

# Fix GhostButtonStyle - add tint parameter
patch(
    'Shared/Theme/ButtonStyles.swift',
    'struct GhostButtonStyle: ButtonStyle {',
    'struct GhostButtonStyle: ButtonStyle {' + NL + '    var tint: Color = .accent'
)
patch(
    'Shared/Theme/ButtonStyles.swift',
    '.foregroundColor(.accent)',
    '.foregroundColor(tint)'
)

# Fix missing UIKit import in NotificationService
patch(
    'Core/Services/NotificationService.swift',
    'import Foundation',
    'import Foundation' + NL + 'import UIKit'
)

print('All patches applied')
