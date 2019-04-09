###How to Set Up DeepChem Environment

1. Install Anaconda3 4.2.0

   - **Notice:** The right version is important.

   - MacOS Version: https://repo.continuum.io/archive/Anaconda3-4.2.0-MacOSX-x86_64.pkg

   - Windows X64 Version: https://repo.continuum.io/archive/Anaconda3-4.2.0-Windows-x86_64.exe

   - Check whether you have installed successfully

     ```
     conda --version
     ```

2. Update Anaconda-client if you cannot open the anaconda navigator

   - Paste the following codes one by one in Terminal(MacOS) or CMD(Windows)

     ```
     conda update anaconda-navigator
     conda update anaconda-client
     conda update -f anaconda-client
     ```

     ​

3. Using a conda environment to install DeepChem

   - Clone deepchem source code from GitHub

     ```
     git clone https://github.com/deepchem/deepchem.git
     ```

   - slow in this step

     ```
     cd deepchem
     bash scripts/install_deepchem_conda.sh deepchem
     ```

   - If your conda version >= 4.4

     ```
     conda activate deepchem
     ```

     Or your conda version < 4.4(If you followed the steps above, the conda version is 4.2.0)

     ```
     source activate deepchem
     ```

   - ```
     yes | pip3 install tensorflow 
     python setup.py install #manual install
     ```

   - Check whether you have installed deepchem successfully

     ```
     nosetests -a '!slow' -v deepchem --nologcapture
     ```

     ​

     ​				

