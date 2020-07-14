'''the training script'''

from argparse import ArgumentParser
from . import LOGGER, set_logging_level


def get_args():
    '''get arguments'''
    parser = ArgumentParser(description='train a text summarization model',
                            prog='PROG')
    subparsers = parser.add_subparsers(help='supported actions')

    parser_train = subparsers.add_parser('train',
                                         help='train the model')

    parser_train.add_argument('config', help='config file', type=str)

    parser_train.set_defaults(func=train)

    parser_predict = subparsers.add_parser('predict',
                                           help='predict for a batch of input')

    parser_predict.add_argument('config', help='config file', type=str)
    parser_predict.add_argument('--test_set',
                                help='name of test set in the config file',
                                type=str)
    parser_predict.add_argument('--output_dir',
                                help='output directory',
                                type=str, default='res')

    parser_predict.set_defaults(func=predict)

    return parser.parse_args()


def train(args):
    # config = load_config(args.config)
    # config['action'] = 'train'
    # model = Model(config)
    # LOGGER.info("starting training process ...")
    # model.build_and_train()
    print('TO BE IMPLETMENTED')


def predict(args):
    # config = load_config(args.config)
    # config['action'] = 'predict'
    # model = Model(config)
    # LOGGER.info("starting predicting process ...")
    # model.load()
    print('TO BE IMPLETMENTED')

def main():
    set_logging_level(logging.INFO)
    args = get_args()
    args.func(args)


if __name__ == "__main__":
    main()
