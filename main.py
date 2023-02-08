import numpy as np
from utils import *


def main(args):
    INPUT_BIN = args.input_path
    OUTPUT_PATH = args.output_path
    LABELS = LABELS_FC if args.classify else LABELS_MD # init the labels

    result = [-1] # default: fail to predict -> -1

    # preprocessing(e.g. reverse to FCG)
    try:
        feature = bin_preprocessing(INPUT_BIN)
    except:
        print('Fail to preprocess.')
        write_output(INPUT_BIN, OUTPUT_PATH, result, LABELS)
        

    # vectorize(feature engineering)
    try:
        feature_vector = vectorize(feature)
    except:
        print('Fail to vectorize.')
        write_output(INPUT_BIN, OUTPUT_PATH, result, LABELS)

    # prediction
    feature_vector = np.array(feature_vector).reshape(1,-1)
    model = load_model(args.model,args.classify)
    result = predict_probabilities(feature_vector,model)
    
    # output
    write_output(INPUT_BIN, OUTPUT_PATH, result, LABELS)

if __name__=='__main__':
    args = parameter_parser()
    main(args)