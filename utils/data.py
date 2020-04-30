import pandas as pd


def load_data(path, label, *features):
    df = pd.read_csv(path)
    return df[list(*features)], df[label]


def fet_lab_names(features, labels):
    assert isinstance(features, pd.DataFrame)
    assert isinstance(labels, pd.Series)
    return list(features.columns), list(map(str, list(labels.unique())))
