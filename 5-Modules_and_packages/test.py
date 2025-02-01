from package.hero import sample
from package.maths import subtr


sample()
print(subtr(2,3))


# to run this test.py file, do the following thing
# 1. first go to the folder where the venv file is located (it is .../python here)
# 3. Then activate the venv (conda actiavte venv/)
# 4. Now go to the folder where this test.py is. (here it is ..../5-Modules_and_pckage)
# 5. Now run "python test.py"


from package.subpackage.subSample import subSampleFunc
subSampleFunc()