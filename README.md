### Environment
* Install Anaconda3
	```zsh
        $ conda create -n venv python=3.7
        $ conda activate venv
        $ conda update -n venv conda
		$ conda install numpy scipy matplotlib spyder pandas seaborn scikit-learn h5py statsmodels

        # like pip freeze
        $ conda env export -n venv > conda_requirements.txt
        $ conda env create -f conda_requirements.txt

		$ python3 check_module.py
	```

