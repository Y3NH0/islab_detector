'''
This file provides the following two functions.
    - parameter_parser
    - write_output

You need to modify the following variables functions.
    - DETECTOR_NAME
    - LABELS_MD
    - LABELS_FC
    - bin_preprocessing
    - vectorize
    - load_model
    - predict_probabilities
'''
import argparse
import os

DETECTOR_NAME = 'GraphTheoryDetector'
LABELS_MD = ['BenignWare','Malware']
LABELS_FC = ['BenignWare', 'Mirai', 'Bashlite', 'Unknown', 'Android', 'Tsunami', 'Dofloo', 'Xorddos', 'Hajime', 'Pnscan']

def parameter_parser():
    '''
    To get the param in cmd

    return. args
        args.input_path : str
        args.output_path : str
        args.classify : bool
        args.model : str
    '''
    # update the description with your detector name
    parser = argparse.ArgumentParser(description='Run ' + DETECTOR_NAME + '.')

    parser.add_argument('-i', '--input-path', type=str, metavar='<path>',
                        help='path to the binary file')

    parser.add_argument('-o', '--output-path', type=str, metavar='<path>', 
                        help='path to the output file')

    # if '-c' in the cmd line then args.classify == True => user wanna do family classification
    # default (-c not in the line) => args.classify == False => user wanna do malware detection
    parser.add_argument('-c', '--classify', action='store_true',
                        help='apply the family classifier')

    parser.add_argument('-m', '--model', type=str, metavar='[ rf | knn | svm | mlp ]', default='mlp',
                        help='model to predict')
    
    args = parser.parse_args()
    return args

def write_output(input_path,output_path,result,labels):
    '''
    param.
        input_path: path to the input binary file
        output_path: path to the csv file
        result: a list(float), probability of each class, e.g. [0.92, 0.08]
        labels: a list(str), each class, e.g. ['Benignware', 'Malware']
    description.
        write a csv file for saving the result of prediction
            e.g.
                FILENAME, Benign, Malware
                34eff01a, 0.98, 0.02
                f01a34ef, 0.17, 0.83
                ff001aff, -1
            or e.g.
                FILENAME, Benign, Mirai, Unknown, Android
                34eff01a, 0.01, 0.02, 0.95, 0.02
                f01a34ef, 0.73, 0, 0.22, 0.05
                ff001aff, -1
    '''

    if '.csv' not in output_path:
        output_path += '.csv'

    # init the columns of this table if it is a new csv file
    if not os.path.exists(output_path):
        with open(output_path,'w') as f:
            line = 'Filename, '
            line += ', '.join(labels)
            line += '\n'
            f.write(line)

    # write the result 
    with open(output_path,'a+') as f:
        line = os.path.basename(input_path) + ', '
        line += ','.join(list(str(i) for i in result))
        line += '\n'
        f.write(line)
    
def bin_preprocessing(input_path:str):
    '''
    param. 
        input_path: path to the input binary
    return.
        feature: e.g. FCG, CFG, Opcode Seq, Header, ...
    '''
    # return feature
    pass

def vectorize(feature):
    '''
    param.
        feature: e.g. FCG, CFG, Opcode Seq, Header, ...
    return.
        feature_vector: e.g. attributes of FCG, Opcode Seq -> doc2vec
    '''
    # return feature_vector
    pass

def load_model(model_name, is_family_classification):
    '''
    param.
        model_name: e.g. rf, mlp
        is_family_classification: boolean, load family clf if it is true
    return.
        model
    '''
    model_path = './FC_Model/' if is_family_classification else './MD_Model/'
    model_path += model_name 
    model_path += '.joblib' # modify to your model format, e.g. pickle
    # model = load(model_path)
    # return model
    pass

def predict_probabilities(feature_vector, model):
    '''
    param.
        feature_vector
    return. 
        the probabilities for each class (family).
    '''
    # result = model.predict_proba(feature_vector).tolist()[0]
    # return result
    pass