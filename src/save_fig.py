import os
import matplotlib.pyplot as plt

def save_fig(name):
    """Save the current Matplotlib figure to the visualizations folder."""
    path = os.path.join('../visualizations', f"{name}.png")
    plt.savefig(path, dpi=300, bbox_inches="tight")
    print(f"Saved: {path}")