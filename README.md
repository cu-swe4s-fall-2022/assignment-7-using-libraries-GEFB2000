# What Assignment 7 Does
Assignment 7 plots iris.data into a scatterplot, boxplot, and combined plot (in plotter.py). Additionally, this assignment contains processing functions within data_processor.py. 

## plotter.py

### get_args()
Makes command line argument for file_name. 

### main()
Plots iris.data into a scatterplot, boxplot, and combined plot. These images are exported to to combined_plot.png, iris_scatter.png, and iris.png.

## data_processor.py

### get_args()
Makes command line argument for file_name, matrix_dimension_1, matrix_dimension_2, and output_dir.

### main()
Calls on get_random_matrix(), get_file_dimensions(), and write_matrix_to_file().

### get_random_matrix()
Takes matrix dimensions from argparse command line arguments to generate a matrix containing random numbers. 

### get_file_dimensions()
Gets the dimensions of the dataset from the iris.data file. Takes in the file. 

### write_matrix_to_file()
Takes the matrix dimensions from argparse to generate a new csv file called np_iris.csv that contains the random matrix. 

## Unit Tests
Unit tests are in test_data_processing.py and continous integration is utilized within the .github/workflows/unit_tests.yml file every time code is pushed to github. 

## Functional Tests
Functional tests are in test_search.sh. There are tests for both plotter.py and data_processor.py. Ryan's ssshtest code is also implemented in the first few lines of code within this file. Continous integration is utilized within the .github/workflows/unit_tests.yml file every time code is pushed to github. 


## Continuous Integration 
environment.yml - sets up conda environment (swe4s) with parameters needed (like matplotlib, pycodestyle, and pandas). 

unit_test.yml - runs unit tests, functional tests, and pycodestyle continuously. 

# How to Use Assignment-7
To use assignment 7, place command line arguments in the run.sh file or command line. These arguments consist of --file_name, --matrix_dimension_1, --matrix_dimension_2, and --output_dir.

# How to Install Software
This software requires the parameters set in environment.yml for installation. 


