<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">Introduction</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li>Prerequisites</a></li>
        <li>Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
      <ul>
        <li>Parsing the data</a></li>
        <li>Training the model</a></li>
        <li>Running predictions</a></li>
      </ul>
  </ol>
</details>



<!-- Introduction -->

### Introduction

GitHub repository for our group's DSA4262 Project. Our group has chosen to use a Random Forest Classifier to identify m6A RNA modifications from direct RNA sequencing data.

<!-- GETTING STARTED -->

## Getting Started

Below are instructions to install the software on an AWS Ubuntu machine.

### Prerequisites
After creating your AWS EC2 instance, 

* To retrieve the latest package lists and give Ubuntu the latest software packages available to install
  ```sh
  sudo apt update
  ```
    
* Install Python
  ```sh
  sudo apt install python3
  ```
  * Verify that Python has been successfully installed
  	```sh
  	python3 --version
  	```
    
* Install Pip, the package installer for Python
  ```sh
  sudo apt install python3-pip
  ```
  * Verify that Pip has been successfully installed
  	```sh
  	pip3 --version
  	```

* Install the prerequisites libraries with Pip
  ```sh
  pip install pandas numpy scikit-learn imbalanced-learn joblib
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/HaoEarm/DSA4262_gartic.git
   ```

<!-- USAGE -->

## Usage

### Parsing the data

### Training the model
* Ensure that you are in **scripts** subfolder
  ```sh
  cd scripts
  ```
* Run the training script to start training the Random Forest Classifier
  ```
  python3 RF_train.py
  ```
* After successful execution, run the prediction script on the test data set
  ```
  python3 RF_test.py
  ```
* A **test_output.csv** should have been created in the **output** subfolder
* In the **output** folder, examine the output prediction file
  ```
  cd ../output/
  head test_output.csv
  ```
  
### Running predictions
* To run predictions on other datasets,  
  1.Run the Data Parsing Scripts on the new raw dataset  
  2.Train / Load a pre-trained model  
  3.Modify RF_predict.py and ensure the filepath and name are correct based on the new input data files, Specifically the line:
  
    	# Reading in the parsed data
        df = pd.read_csv('../Data/test_data.csv') # Edit File name to relevant csv file
  4.Run RF_predict.py and examine the output.csv in the output subfolder
