## NOTE: This code is a extract from https://github.com/malfante/AAA. 
This code calculates the feature vector from a MSEED file to used it later for training and classification purposes. 


# Automatic Analysis Architecture 

Welcome to this automatic classification scheme! Please carefully read the following before asking questions :)

If used, the software should be credited as follow:    

**Automatic Analysis Architecture, M. MALFANTE, J. MARS, M. DALLA MURA**   
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1216028.svg)](https://doi.org/10.5281/zenodo.1216028)   

and the original paper for which the code was developped should be cited:   

**Malfante, M., Dalla Mura, M., Metaxian, J. P., Mars, J. I., Macedo, O., & Inza, A. (2018). Machine Learning for Volcano-Seismic Signals: Challenges and Perspectives. IEEE Signal Processing Magazine, 35(2), 20-30.**  

We thank you for the respect of the authors work.

## Set up and requierements needed to run the code
This code was developed under Python 3, and needs the following libraries. .

- `obspy>=1.1`
- `python_speech_features`
- `sympy`


Create and activate your working environment (in a terminal session):  

`conda create -n aaa_features python=3.9`  
`conda activate aaa_features`

# Clone the repository and install 

`git clone https://github.com/awacero/aaa_features.git` 

`cd aaa_features` 

`pip install .` 


# Install the package aaa_features from PYPI:

`pip install aaa_features`  


## Configuration files 
	 	
- the feature setting file, contained in `config_sample/features*.json` 

## MSEED data sample
- the folder data_sample contains a MSEED file from the station EC RETU SHZ 2012-06-28

## Run the code to get the features

`python call_aaa_features.py`

## More info	

If you still have questions, try running and exploring the code. 
The playground files are relatively easy to play with. 

If you still have question, fell free to ask ! 

**Contact:** marielle.malfante@gmail.com

