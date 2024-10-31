
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
        <li>Data parsing and processing</a></li>
        <li>Training the model</a></li>
        <li>Running predictions</a></li>
      </ul>
  </ol>
</details>



<!-- Introduction -->

### Introduction

Welcome to the GitHub repository for our group's DSA4262 Project. Our group has chosen to use a Random Forest Classifier to identify m6A RNA modifications from direct RNA sequencing data.

<!-- GETTING STARTED -->

## Getting Started

Below are instructions to install the software on an AWS Ubuntu machine. When starting your AWS Ubuntu instance, we recommend an Instance Type of at least t3.xlarge.

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
* For the demostration in this repository, all of the scripts were ran on dataset0 as provided in DSA4262 Canvas Module.

### Data parsing and processing
* Ensure that you are in **scripts** subfolder
  ```sh
  cd DSA4262_gartic/scripts
  ```

* Due to file size limitations, this repository is unable to host the dataset0 for the parsing and processing scripts to run on. You do not need to run the parsing scripts to run the method (prediction script) on a test data set which is provided for the method in the next section.

* Please ensure the filepaths are correct based on your raw data, For example if using dataset0, you will need to update the input data files into the relevant lines of code in the script
	```
	data_parsing_updated.py
	Input Data: dataset0.json, data_info_labelled.csv
	Outputs: parsed_json.csv
	```

* Run the data parsing script to read the json file
  ```sh
  python3 data_parsing_updated.py
  ```
  
* Run the data processing script to process the parsed data and data labels
  ```sh
  python3 data_processing_updated.py
  ```
  
### Training the model
* Run the training script to start training the Random Forest Classifier
  ```
  python3 RF_train.py
  ```
* A model will be saved in the *model* subfolder and can be loaded to run predictions.

### Predicting on a dataset

The **model** folder already has a saved model inside, and can be loaded to run predictions for m6A probabilities on a test data set, which is also provided in this repository.
In the **scripts** subfolder, run the script to predict m6A probabilities on the provided test data set
  ```
  python3 RF_predict.py
  ```
* A **output.csv** should have been created in the **output** subfolder

* In the **output** folder, examine the output prediction file
  ```
  cd ../output
  head output.csv
  ```
  
### Running predictions (In a Nutshell)
* To run predictions on a dataset,  
  1. Run the Data Parsing Scripts on the dataset  
  2. Train / Load a pre-trained model  
  3. Modify RF_predict.py and ensure the filepath and name are correct based on the input data files
  4. Run RF_predict.py and examine the output.csv in the **output** subfolder

