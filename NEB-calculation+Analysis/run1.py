import sys
import numpy
#import detector
import glob
#import center
import matplotlib as plt
import subprocess
import Gnuplot, Gnuplot.PlotItems, Gnuplot.funcutils
import os
g=Gnuplot.Gnuplot(debug=1)
orig=os.path.abspath('.')
print ('Current directory :',orig)
i=1
for filename in glob.glob(orig+"/555-111pka-fixxyz-min-neb-1/"):
    
                          os.chdir(filename)
                          print ('new directory: ',filename)
                          subprocess.call(['./GetResults.sh',filename])
                          print('end')
                          Einit=-1072.9795
                          g('set ylabel "Energy (eV)"')
                          g('set xlabel "Reaction coordinate"')
                          g('set term png')
                          j="neb-band-"+str(i)+".png"
                          print(j)
                          g('set output "'+j+'"')
                          #for file in glob.glob(filename+"*.txt"):
                          #print('file :',file)
                              #databuff=Gnuplot.File(file,using='1:2',with_='line',title='optimised path')
                              #g.plot(databuff)
#g.plot(Gnuplot.File(file,using='1:($2--1072.9795)',with_='linespoints',title=file))
#g('replot')

                          filename1=filename+"resultsInitial.txt"
                          filename2=filename+"resultsFinal.txt"
                          #print(' inital text', filename1)
                          g.plot(Gnuplot.File(filename1,using='1:2',with_='linespoints',title='Interpolated Path'),Gnuplot.File(filename2,using='1:2',with_='linespoints',title='Optimised Path'))
                          #g('replot')
                          print('back to original ',orig)
                          i+=1
#os.chdir(orig)
