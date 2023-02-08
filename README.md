# YOUR_DETECTOR_NAME

> ref. YOUR_REF_PAPER

## Attributes

### Model(Classifier)

### Feature



## Usage
* unzip models to `FC_Model` and `MD_Model`: `make`
* input binary: `-i <path>`, `--input-path <path>`
* model: `-m <model>`, `--model <model>`
  * rf, MODEL_4, MODEL_2, MODEL_3
* output (record): `-o <path>`, `--output-path <path>`
* Malware Detection / Family Classification
    * do nothing if you wanna do malware detection(binary clf)  
    * add `-c` if you wanna do family classification 
* e.g.
    `python main.py -i testingBin/0021eaf2 -o myDetector_FC_records.csv -m rf -c`
    * using trained rf family classifier(`-c`), predict '0021eaf2' and write the result to 'myDetector_FC_records.csv'
    * add `-W ignore` if you keep getting bothered by warning msg

### Note
* a output csv file for a experiment
  * e.g.
    
    ```python=
    for bin in bins:
      cmd = 'python main.py -i ' + bin
      cmd += ' -m rf -o GraphTheoryDetector_RF_MD.csv'
      os.system(cmd)
    ```
    specify another output file if you wanna do FC task or you wanna change the model
* output file format

  |    Filename  | Benignware | Malware |
  | :----------: | :------: | :-------: |
  | 00ffe391     |   0.97   |   0.03    |
  |     00f391fe      |  0.967   |  165.51   |
  |     1fe00f39      |  -1   |    |
  * it will record the prob of each class
  * -1 means fail

## Model Performance
* Malware Detection
  |    Models    | Accuracy | Time cost |
  | :----------: | :------: | :-------: |
  |     MODEL_1  |   0.97   |   5.01    |
  |     MODEL_2  |  0.967   |  165.51   |
  |     MODEL_3  |  0.772   |  1606.21  |

* Family Classification
  |    Models    | Accuracy | Time cost |
  | :----------: | :------: | :-------: |
  |     MODEL_1  |  0.952   |   4.21    |
  |     MODEL_2  |  0.944   |  104.92   |
  |     MODEL_3  |   0.71   |  1562.06  |
