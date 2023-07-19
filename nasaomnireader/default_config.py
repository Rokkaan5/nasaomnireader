# (C) 2020 University of Colorado AES-CCAR-SEDA (Space Environment Data Analysis) Group
# Written by Liam M. Kilcommons
import os

#Determine where this module's source file is located
src_file_dir = os.path.dirname(os.path.realpath(__file__))

data_dir = os.path.join(src_file_dir,'cuseda')

print('Solar wind data files will be saved to {}'.format(data_dir))
if not os.path.exists(data_dir):
    print('Created {}'.format(data_dir))
    os.makedirs(data_dir)

config = {
    'omnireader' : {
        'local_cdf_dir':data_dir
    }
}
