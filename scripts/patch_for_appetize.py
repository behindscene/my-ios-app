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

# Fix named colors in AppTheme.swift - hardcode values to avoid xcassets dependency
theme = 'Shared/Theme/AppTheme.swift'
patch(theme, 'Color("BgBase")',        'Color(red:0.039,green:0.039,blue:0.039)')
patch(theme, 'Color("BgSurface")',      'Color(red:0.067,green:0.067,blue:0.067)')
patch(theme, 'Color("BgElevated")',     'Color(red:0.102,green:0.102,blue:0.102)')
patch(theme, 'Color("BgOverlay")',      'Color(red:0.133,green:0.133,blue:0.133)')
patch(theme, 'Color("BorderSub")',      'Color(red:0.122,green:0.122,blue:0.122)')
patch(theme, 'Color("BorderMain")',     'Color(red:0.180,green:0.180,blue:0.180)')
patch(theme, 'Color("TextPrimary")',    'Color(red:1.0,green:1.0,blue:1.0)')
patch(theme, 'Color("TextSecondary")',  'Color(red:0.533,green:0.533,blue:0.533)')
patch(theme, 'Color("TextTertiary")',   'Color(red:0.290,green:0.290,blue:0.290)')
patch(theme, 'Color("Accent")',         'Color(red:0.039,green:0.729,blue:0.710)')
patch(theme, 'Color("AccentLight")',    'Color(red:0.071,green:0.808,blue:0.784)')
patch(theme, 'Color("AccentMuted")',    'Color(red:0.039,green:0.729,blue:0.710).opacity(0.15)')
patch(theme, 'Color("AccentFg")',       'Color(red:0.0,green:0.0,blue:0.0)')
patch(theme, 'Color("Positive")',       'Color(red:0.063,green:0.725,blue:0.506)')
patch(theme, 'Color("Warning")',        'Color(red:0.961,green:0.620,blue:0.043)')
patch(theme, 'Color("Negative")',       'Color(red:0.937,green:0.267,blue:0.267)')
patch(theme, 'Color("Surface")',        'Color(red:0.067,green:0.067,blue:0.067)')
patch(theme, 'Color("SurfaceElevated")', 'Color(red:0.102,green:0.102,blue:0.102)')
patch(theme, 'Color("Border")',         'Color(red:0.180,green:0.180,blue:0.180)')
patch(theme, 'Color("Destructive")',    'Color(red:0.937,green:0.267,blue:0.267)')
patch(theme, 'Color("Success")',        'Color(red:0.063,green:0.725,blue:0.506)')

print('All patches applied')
