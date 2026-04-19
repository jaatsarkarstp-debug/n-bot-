from ursina import *

app = Ursina()

# High-end Environment
Entity(model='sphere', scale=500, double_sided=True, texture='sky_sunset', rotation=(0,90,0))
EditorCamera() # For development

class Block(Button):
    def __init__(self, position=(0,0,0), color=color.azure):
        super().__init__(
            parent=scene,
            model='cube', # Replace with a high-poly .obj rounded cube
            color=color,
            position=position,
            scale=0.9,
            highlight_color=color.light(0.2),
            pressed_color=color.darker(0.2)
        )
        # Add a "glow" child entity
        self.glow = Entity(parent=self, model='cube', scale=1.1, color=color, alpha=0.1)

    def on_mouse_enter(self):
        self.animate_scale(1.1, duration=0.1)
        
    def on_mouse_exit(self):
        self.animate_scale(0.9, duration=0.1)

# Generate a high-fidelity grid
grid = []
for x in range(8):
    for y in range(8):
        grid.append(Block(position=(x, y, 0), color=color.black66))

app.run()
