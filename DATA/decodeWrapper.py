# Written by Minnie Hyemin Yoo 7/3/18
# This file is a wrapper file to call the ruby command to decode the 
# sl2 file and then takes the data
import subprocess

test = subprocess.Popen(["ruby","sl2decode.rb","Sonar0000TEST.sl2"])
output = test.communicate()[0]
