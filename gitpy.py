#!/Users/Naman/miniconda/bin/python

# importing standard modules
import re,inspect,os,sys;

# some boiler plate code.
poing = inspect.getabsfile(inspect.currentframe());
ee=execfile;
selfdir=os.path.dirname(poing);
os.chdir(selfdir);

# start here..
samps = "This is sparta";
sampl = ["Elon","Musk","Steve","Jurvetson"];
sampd = {"Python":"is Great","Tesla":"Motors"};

testchange = "This is testing change"



