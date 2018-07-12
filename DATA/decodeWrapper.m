s = system('ruby sl2decode.rb Sonar0000TEST.sl2'); % this executes the command
M = csvread('Sonar0000TEST.sl2_output_raw.csv',0,0);