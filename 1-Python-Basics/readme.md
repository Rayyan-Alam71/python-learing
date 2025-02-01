# terminal itself provides kernel for executing the program , there we dont need any kernel here



# different ways of creating python environment
    #1 =>
        # python -m venv myenv (my folder name)
        # myenv/Scripts/activate (to activate the env.)
    
    #2 => (for linux os)
        virtualenv -p python3 virtual-env-name
        for actiavtion : virtual-env-name/Scripts/activate 

    #3 => 
        conda create -p venv python==3.12
        conda activate venv/


# for installing the jupyter notebook
    select venv env(go to the path in the terminal)
    pip install ipykernel




### Variables
    Variables are findamental elements in prgramming used to store data that can be referenced and amaniplated in a program. In Python, variables are cerated when yiu assign value to them, and they do notneed explicit declaration to reservee memory space. The decalaration hapens autom..

    ## Naming Cnvention
        # Variable names should be descriptive
        # thet must always start with a letter or an underscore
        # can contain letters, numbers and/or underscore
        # Variables names are case sensitive
    ## Understanding variable types
        # Python is dynamically types, that is a type of a variable is defined at rntime


# While downloading the numpy folder I faced the issue of "Requirement already satisfied: pure-eval in c:\users\aio\onedrive\desktop\python\venv\lib\site-packages (from stack_data->ipython>=7.23.1->ipykernel->-r requirements.txt (line 1)) (0.2.3)"

To tackle this , first go to the root folder (folder consisting the venv folder), then activate the venv env. (conda activate venv/) then do the installation 
    This should work
    