#!bin/sh

set -e
set -u
set -o pipefail

python data_processor.py --matrix_dimension_1 4 --matrix_dimension_2 5 --file_name 'iris.data' --output_dir 'matrix.png' 

python plotter.py --file_name 'iris.data'

python test_data_processor.py

bash test_search.sh