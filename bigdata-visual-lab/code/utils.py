import pandas as pd, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA1 = os.path.join(BASE, "data", "第二章 图表(前15).xlsx")
DATA2 = os.path.join(BASE, "data", "第二章 图表(后15).xlsx")
OUT = os.path.join(BASE, "outputs")
os.makedirs(OUT, exist_ok=True)
def read_sheet(path, sheet_name, skiprows=2):
    return pd.read_excel(path, sheet_name=sheet_name, skiprows=skiprows)
def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, name), dpi=150)
    import matplotlib.pyplot as plt
    plt.close(fig)