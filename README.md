# Islab Detector Guideline

1. Train your detector and save it to `FC_model` or `MD_model`.
    - include binary classifier (for malware detection) and multi-class classifier (for family classification)

2. Modify the following functions in `utils.py`
    ```
    bin_preprocessing
    vectorize
    load_model
    predict_probabilities
    ```
3. try to run the `main.py` (or modify `test_script.py` and run it)

4. modify `README.md` s.t. people who use your detector can easily realize the attributes and the usage