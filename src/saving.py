from src.globals import BASE_DIR

FIGURE_DIR = BASE_DIR + 'figures/'
def save_figure(fig, name):
    path = FIGURE_DIR + name
    fig.savefig(path, format='pdf', bbox_inches="tight")