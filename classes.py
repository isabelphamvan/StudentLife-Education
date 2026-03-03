# %%
import pandas as pd

def load_classes(path="/Users/isabel/StudentLife-Education/class.csv"):
    rows = []
    with open(path) as f:
        for line in f:
            parts = line.strip().split(',')
            uid = parts[0]
            for c in parts[1:]:
                if c:
                    rows.append({'uid': uid, 'class': c.strip()})
    return pd.DataFrame(rows)

# %%
df_classes = load_classes()
df_classes
