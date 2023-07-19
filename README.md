Forked copy of Liam Kilcommons' nasaomnireader package

Orginal repo here:[https://github.com/lkilcommons/nasaomnireader]

---
### Data Sources ###

The package automatically downloads data from the NASA OMNIWeb website. It can use data in two formats:

#### Text ####

By default, text files are downloaded and used. 

    WARNING: metadata for text files is supplied from hardcoded, dumped CDF file metadata
  
#### CDF ####

The NASA CDF format files will be downloaded if the code finds the following packages on your computer:

1. [The NASA CDF Library](http://cdf.gsfc.nasa.gov/)

2. [Spacepy](https://pypi.python.org/pypi/SpacePy), for it's pyCDF python interface to the NASA CDF Library
