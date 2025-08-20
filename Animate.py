import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import matplotlib
from collections import Counter

# Use emoji-capable font (adjust for your OS)
matplotlib.rcParams['font.family'] = 'Segoe UI Emoji' 


ICON_MAP = {
    "police": "👮",
    "thief": "🦹",
    "father": "👨",
    "mother": "👩",
    "son": "👦",
    "daughter": "👧"
}

class AnimateRiver:
    def __init__(self, path):
        self.path = path
        self.index = 0
        self.final_depth = path[-1].depth if path else 0

        # Create figure
        self.fig, self.ax = plt.subplots(figsize=(10, 5))
        plt.subplots_adjust(bottom=0.2)  # leave space for button
        self.ax.set_xlim(0, 12)
        self.ax.set_ylim(0, 8)
        self.ax.axis('off')

        # Add "Next" button
        axnext = plt.axes([0.45, 0.05, 0.1, 0.075])  # x, y, width, height
        self.btn_next = Button(axnext, 'Next')
        self.btn_next.on_clicked(self.next_step)

        # Draw first state
        self.draw_state(self.path[self.index])

    

    def get_boat_passengers(self, state):
        """Find who moved between parent and current state (handles duplicates)"""
        if state.parent is None:
            return []

        if state.is_boat_on_left:  # Boat just arrived to left
            # They left the parent's right side
            before = Counter(state.parent.right_side)
            after = Counter(state.right_side)
        else:  # Boat just arrived to right
            before = Counter(state.parent.left_side)
            after = Counter(state.left_side)

        # Passengers = who disappeared from origin side
        moved = []
        for person, count in before.items():
            diff = count - after.get(person, 0)
            if diff > 0:
                moved.extend([person] * diff)

        return moved

    def draw_state(self, state):
        self.ax.clear()
        self.ax.set_xlim(0, 12)
        self.ax.set_ylim(0, 8)
        self.ax.axis('off')

        # Draw background
        self.ax.fill_between([5, 7], 0, 8, color='skyblue', alpha=0.6)  # river
        self.ax.fill_between([0, 5], 0, 8, color='lightgreen', alpha=0.5)  # left land
        self.ax.fill_between([7, 12], 0, 8, color='wheat', alpha=0.5)      # right land

        # Left side people
        for i, person in enumerate(state.left_side):
            icon = ICON_MAP.get(person, person)
            self.ax.text(1, 7 - i, icon, fontsize=25)

        # Right side people
        for i, person in enumerate(state.right_side):
            icon = ICON_MAP.get(person, person)
            self.ax.text(11, 7 - i, icon, fontsize=25)

        # Boat
        if state.is_boat_on_left:
            self.ax.text(4.5, 1, "⛵", fontsize=40)
        else:
            self.ax.text(7.5, 1, "⛵", fontsize=40)

        # Who traveled
        passengers = self.get_boat_passengers(state)
        if passengers:
            passenger_icons = " ".join(ICON_MAP.get(p, p) for p in passengers)
            self.ax.text(6, 0.5, f"On boat: {passenger_icons}", fontsize=14, ha="center")

        # Title
        if state == self.path[-1]:
            self.ax.set_title(f"Goal reached! Depth = {self.final_depth}", 
                              fontsize=16, weight="bold", color="darkred")
        else:
            self.ax.set_title(f"Step {state.depth} / {self.final_depth}", 
                              fontsize=16, weight="bold", color="darkblue")

        self.fig.canvas.draw_idle()

    def next_step(self, event):
        if self.index < len(self.path) - 1:
            self.index += 1
            self.draw_state(self.path[self.index])
