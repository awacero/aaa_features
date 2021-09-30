# Automatic Analysis Architecture 

Welcome to this automatic classification scheme! Please carefully read the following before asking questions :)

If used, the software should be credited as follow:    

**Automatic Analysis Architecture, M. MALFANTE, J. MARS, M. DALLA MURA**   
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1216028.svg)](https://doi.org/10.5281/zenodo.1216028)   

and the original paper for which the code was developped should be cited:   

**Malfante, M., Dalla Mura, M., Metaxian, J. P., Mars, J. I., Macedo, O., & Inza, A. (2018). Machine Learning for Volcano-Seismic Signals: Challenges and Perspectives. IEEE Signal Processing Magazine, 35(2), 20-30.**  

We thank you for the respect of the authors work.

## Set up and requierements needed to run the code
This code was developed under Python 3, and needs the following libraries. Those libraries need to be previously installed.

- `obspy==1.1`
- `python_speech_features`
- `sympy`


Create and activate your working environment (in a terminal session):  
`conda create -n aaa_features python=3.9`  
`conda activate aaa_features`

Install the library aaa_features
`pip install aaa_features`  


Run the code (see next section)





 


## Configuration files 
	 	
All the settings related to a new project or a new run are indicated in a setting main setting. 

It contains information regarding the project paths, the considered application, the signals preprocessing, the features used (linked to a dedicated feature configuration file), and the learning algorithms. 

Extra information regarding the wanted analysis, the data to analyze and display parameters are indicated in a separate configuration file, which format depends on the usecase. 

So, for each configuration, 3 configuration files are considered:

- the general setting file, contained in `config/general` folder
- the feature setting file, contained in `config/specific/features` folder
- the configuration file specific to the wanted analysis, contained in `config/specific/usecaseXX/`

Commented examples for each of the setting files are available (but keep in mind that json files do not support comments, so those files are simply there as examples.)


## More info	

If you still have questions, try running and exploring the code. 
The playground files are relatively easy to play with. 

If you still have question, fell free to ask ! 

**Contact:** marielle.malfante@gmail.com

