import sys
import qdarktheme
import furniture_converter

from PyQt6.QtWidgets import (
    QApplication, QLabel, QWidget, QVBoxLayout,
    QHBoxLayout, QLineEdit, QPushButton)

def go_button_clicked():
    furniture_converter.main(modNameLineEdit.text(), authorLineEdit.text(),
                             originalLineEdit.text(), outputLineEdit.text(),
                             sellAtLineEdit.text())

app = QApplication([])
qdarktheme.setup_theme()
window = QWidget()
window.setWindowTitle("Custom Furniture to DGA Converter")
window.setFixedHeight(200)
window.setMinimumWidth(600)
windowLayout = QVBoxLayout()
authorForm = QHBoxLayout()
modNameForm = QHBoxLayout()
originalForm = QHBoxLayout()
outputForm = QHBoxLayout()
sellAtForm = QHBoxLayout()
goButtonLayout = QHBoxLayout()

minLabelWidth = 70

# Mod author elements
authorLabel = QLabel("Author")
authorLabel.setMinimumWidth(minLabelWidth)
authorLineEdit = QLineEdit()
# Mod name elements
modNameLabel = QLabel("Mod name")
modNameLabel.setMinimumWidth(minLabelWidth)
modNameLineEdit = QLineEdit()

# Original elements
originalBrowseButton = QPushButton("Browse")
originalLabel = QLabel("Original")
originalLabel.setMinimumWidth(minLabelWidth)
originalLineEdit = QLineEdit()

# Output elements
outputBrowseButton = QPushButton("Browse")
outputLabel = QLabel("Output")
outputLabel.setMinimumWidth(minLabelWidth)
outputLineEdit = QLineEdit()

# Sell at elements
sellAtLabel = QLabel("Sell at")
sellAtLabel.setMinimumWidth(minLabelWidth)
sellAtLineEdit = QLineEdit()

# Go button elements
goButton = QPushButton("Start")

# Setting up the root layouts
window.setLayout(windowLayout)
windowLayout.addLayout(authorForm)
windowLayout.addLayout(modNameForm)
windowLayout.addLayout(originalForm)
windowLayout.addLayout(outputForm)
windowLayout.addLayout(sellAtForm)
windowLayout.addLayout(goButtonLayout)

# Adding things to the layouts
authorForm.addWidget(authorLabel)
authorForm.addWidget(authorLineEdit)

modNameForm.addWidget(modNameLabel)
modNameForm.addWidget(modNameLineEdit)

originalForm.addWidget(originalLabel)
originalForm.addWidget(originalLineEdit)
originalForm.addWidget(originalBrowseButton)

outputForm.addWidget(outputLabel)
outputForm.addWidget(outputLineEdit)
outputForm.addWidget(outputBrowseButton)

sellAtForm.addWidget(sellAtLabel)
sellAtForm.addWidget(sellAtLineEdit)

goButtonLayout.addWidget(goButton)

goButton.clicked.connect(go_button_clicked)

window.show()

sys.exit(app.exec())
