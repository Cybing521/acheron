# Source Generated with Decompyle++
# File: tmp58y05682.marshal (Python 3.11)

self.buttons = {
    (255, 255, 255): self.whiteButton,
    (255, 0, 0): self.redButton,
    (0, 255, 0): self.greenButton,
    (0, 0, 255): self.blueButton,
    (0, 255, 255): self.cyanButton,
    (255, 0, 255): self.magentaButton,
    (255, 255, 0): self.yellowButton,
    (0, 0, 0): self.blackButton }
self.whiteButton.clicked.connect(self.white_button_pressed)
self.redButton.clicked.connect(self.red_button_pressed)
self.greenButton.clicked.connect(self.green_button_pressed)
self.blueButton.clicked.connect(self.blue_button_pressed)
self.cyanButton.clicked.connect(self.cyan_button_pressed)
self.magentaButton.clicked.connect(self.magenta_button_pressed)
self.yellowButton.clicked.connect(self.yellow_button_pressed)
self.blackButton.clicked.connect(self.black_button_pressed)
self.redSlider.valueChanged.connect(self.color_changed)
self.greenSlider.valueChanged.connect(self.color_changed)
self.blueSlider.valueChanged.connect(self.color_changed)
