import argparse

import numpy as np
from sklearn.preprocessing import LabelEncoder

from utils.data import load_data
from utils.model import train_model, load_model
from utils.plot import plot_graph, plot_pca


def parse_args():
    def str2bool(v):
        if isinstance(v, bool):
            return v
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected')

    parser = argparse.ArgumentParser()

    parser.add_argument('--load', type=str2bool, default=False,
                        help='True: Load trained model  False: Train model default: True')
    parser.add_argument('--gs', type=str2bool, default=False,
                        help='Find optimal parameters with 10-Fold GridSearchCV')

    parser.print_help()

    return parser.parse_args()


if __name__ == '__main__':
    np.random.seed(1)

    args = parse_args()

    features, labels = load_data('data/iris_data.csv', 'Class',
                                 ('SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'))
    plot_pca(features, LabelEncoder().fit_transform(labels))

    if args.load:
        model = load_model('weights/AdaBoost-hgzmu.pkl')
        plot_graph(model, features, labels, 'adaboost-graph-')
        sepalLength, sepalWidth, petalLength, petalWidth = 5.4, 3.7, 1.5, 0.2
        print(model.predict([list((sepalLength, sepalWidth, petalLength, petalWidth))])[0])
    else:
        model = train_model(features, labels,args)

        sepalLength, sepalWidth, petalLength, petalWidth = 5.4, 3.7, 1.5, 0.2
        print(model.predict([list((sepalLength, sepalWidth, petalLength, petalWidth))])[0])
