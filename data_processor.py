import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import argparse

def get_args():
    '''
    Functions: 
    * get_args - makes command line arguments implemented in the shell script but can also be used in the terminal.
    
    
    Parameters:
    * --file_name: file name that contains the iris data (iris.data in our case)
    * --matrix_dimension_1: first dimension of matrix
    * --matrix_dimension_2: second dimension of matrix
    * --output_dir: output directory
    
    Returns:
    * parser.parse_args() - allows for command line arguments
    '''
    parser = argparse.ArgumentParser(
                    description = 'NumPy practice',
                    prog = 'assignment 7')
    parser.add_argument('--matrix_dimension_1', 
                        type = int,
                        help = 'dimensions of matrix')
    parser.add_argument('--matrix_dimension_2', 
                        type = int,
                        help = 'dimensions of matrix')
    parser.add_argument('--file_name',
                        type = str,
                        help = 'iris data file')
    parser.add_argument('--output_dir',
                       type = str,
                       help = 'output directory')
    
    return parser.parse_args()

def main():
    '''
    Functions: 
    * main - calls on get_random_matrix, get_file_dimensions, and write_matrix_to_file to print to screen & write to a new file called 'np_iris.csv'
    '''
    args = get_args()    
    
    print(get_random_matrix(args.matrix_dimension_1,args.matrix_dimension_2))
    print(get_file_dimensions(args.file_name))
    write_matrix_to_file(args.matrix_dimension_1,args.matrix_dimension_2,args.output_dir)

def get_random_matrix(num_rows, num_columns):
    '''
    Functions:
    * get_random_matrix: uses NumPy to generate a seed and a random matrix of numbers
    
    Parameters:
    * num_rows - matrix dimension 1
    * num_columns - matrix dimension 2
    
    Returns: a random matrix, dimensions put into command line argparse
    '''
    #assert like the matrix dimensions, assert entire list is of length 4 etc..
    np.random.seed(7)
    return np.random.rand(num_rows,num_columns)

def get_file_dimensions(file_name):
    '''
    Functions: 
    * get_file_dimensions: gets the dimensions of dataset (iris.data)
    
    Parameters:
    * file_name - name of file that the user wants to get the dimensions of
    
    Returns: the dimensions of a dataset
    '''
    iris_df = pd.read_csv(file_name,sep=',')
    iris_df.columns = ['sepal_width','sepal_length','petal_width','petal_length','species']
    return iris_df.shape

def write_matrix_to_file(num_rows, num_columns, output_file):
    '''
    Functions:
    * write_matrix_to_file: writes random matrix to a new csv file called 'np_iris.csv'
    
    Parameters:
    * num_rows - matrix dimension 1
    * num_columns - matrix dimension 2
    * output_file - the file that the matrix will be placed in (np_iris.csv)
    
    Returns: iris, which is a variable for the random matrix
    '''
    np.random.seed(7)
    iris = np.random.rand(num_rows,num_columns)
    np.savetxt('np_iris.csv',iris,delimiter=',')
    print(iris.tolist())
    return iris
    
if __name__ == '__main__':
    main()