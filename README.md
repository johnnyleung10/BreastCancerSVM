# BreastCancerSVM

Predicts whether a tumor is 'benign' or 'malignant' using a SVM model in Machine Learning.

## Getting Started

First install TensorFlow and Anaconda. You can follow the following tutorial https://docs.anaconda.com/anaconda/user-guide/tasks/tensorflow/

### Installing

Open the Project in PyCharm and change the project interpreter in Project Settings to "pythonw.exe" in the Anaconda installation folder.

Then install the following python packages in the Anaconda enviorment.

```
pip install tensorflow
```

```
pip install sklearn
```

```
pip install pickle
```

```
pip install numpy
```

```
pip install keras
```
Now that the enviorment is setup, you can simply run the BreastCancerSVM.py file.

## Built With

* [TensorFlow](https://www.tensorflow.org/) - The Machine Learning Platform used
* [Anaconda](https://www.anaconda.com/) - Python Package Installer
* [SKLearn](https://scikit-learn.org/stable/) - Used to generate models

## Data

| | Attribute      | Domain          | 
|- | :------------- |:------------- | 
|1 | Sample code number    | id number | 
|2| Clump Thickness      | 1 - 10     |  
|3| Uniformity of Cell Size | 1 - 10      |  
|4| Uniformity of Cell Shape    | 1 - 10 | 
|5| Marginal Adhesion     | 1 - 10      |  
|6| Single Epithelial Cell Size   | 1 - 10      |  
|7| Bare Nuclei   | 1 - 10 | 
|8| Bland Chromatin     | 1 - 10      |  
|9| Normal Nucleoli  | 1 - 10     |  
|10| Mitoses   | 1 - 10    |  
|11| Class | (2 for benign, 4 for malignant)      |  

## Acknowledgements

This breast cancer databases was obtained from the University of Wisconsin
   Hospitals, Madison from Dr. William H. Wolberg.  If you publish results
   when using this database, then please include this information in your
   acknowledgements.  Also, please cite one or more of:

   1. O. L. Mangasarian and W. H. Wolberg: "Cancer diagnosis via linear 
      programming", SIAM News, Volume 23, Number 5, September 1990, pp 1 & 18.

   2. William H. Wolberg and O.L. Mangasarian: "Multisurface method of 
      pattern separation for medical diagnosis applied to breast cytology", 
      Proceedings of the National Academy of Sciences, U.S.A., Volume 87, 
      December 1990, pp 9193-9196.

   3. O. L. Mangasarian, R. Setiono, and W.H. Wolberg: "Pattern recognition 
      via linear programming: Theory and application to medical diagnosis", 
      in: "Large-scale numerical optimization", Thomas F. Coleman and Yuying
      Li, editors, SIAM Publications, Philadelphia 1990, pp 22-30.

   4. K. P. Bennett & O. L. Mangasarian: "Robust linear programming 
      discrimination of two linearly inseparable sets", Optimization Methods
      and Software 1, 1992, 23-34 (Gordon & Breach Science Publishers).






