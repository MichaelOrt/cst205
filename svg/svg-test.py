import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSvg import QSvgWidget

svg_str = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="498" height="497"
        viewBox="-0.5 0 498 497" enable-background="new -0.5 0 498 497" xml:space="preserve">
<circle fill="#FFFF00" stroke="#000000" stroke-width="15" cx="248.5" cy="248.5" r="241"/>
<ellipse cx="144.166" cy="180.166" rx="44" ry="53.833"/>
<ellipse cx="337.666" cy="180.166" rx="44" ry="53.833"/>
<path d="M425.834,298c-14.334,20.5-78.127,131.167-174.5,131.167c-96.374,0-145.833-81.667-174.5-131.167
        c53.167,18.5,92.583,35.667,174.5,35.667C333.251,333.667,398.5,306.5,425.834,298z"/>
</svg> 
"""
# ==========================================
with open('smile.svg', 'w') as f:
    f.write(svg_str)
# ==========================================
app = QApplication(sys.argv)
svgWidget = QSvgWidget('smile.svg')
svgWidget.setGeometry(100,100,800,800)
svgWidget.show()
sys.exit(app.exec_())