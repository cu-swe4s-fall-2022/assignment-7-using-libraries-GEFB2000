import matplotlib.pyplot as plt
import pandas as pd
import argparse

def get_args():
    '''
    Functions: 
    * get_args - makes command line arguments implemented in the shell script but can also be used in the terminal.
    
    
    Parameters:
    * --file_name: file name that contains the iris data (iris.data in our case)
    
    Returns:
    * parser.parse_args() - allows for command line arguments
    '''
    parser = argparse.ArgumentParser(
                    description = 'NumPy practice',
                    prog = 'assignment 7')
    parser.add_argument('--file_name',
                        type = str,
                        help = 'iris data file')
    return parser.parse_args()

def main():
    '''
    Functions:
    * main - creates boxplot that plots sepal_width, sepal_length, petal_width, petal_length by their length in centimeters. Also creates a scatterplot that plots sepal_length by sepal_width. Lastly, the function takes these two plots and puts them in a multipanel. 
    
    Parameters:
    * --file_name: file name that contains the iris data (iris.data in our case)
    
    Returns:
    * iris_scatter.png - scatter plot
    * iris.png - box plot
    * combined_plot - multipanel with scatter and boxplot
    '''
    args = get_args()

    iris = pd.read_csv(args.file_name)
    
    iris.columns = ['sepal_width',
                    'sepal_length',
                    'petal_width',
                    'petal_length',
                    'species']
    measurement_names = ['sepal_width',
                         'sepal_length',
                         'petal_width',
                         'petal_length']
    
    plt.boxplot(iris[measurement_names], labels = measurement_names)
    plt.ylabel('cm')
    plt.show()
    plt.savefig('iris.png')
    
    fig, axes = plt.subplots(1, 2)
    iris_data = pd.read_csv(args.file_name)
    iris_data.columns = ['sepal_width',
                         'sepal_length',
                         'petal_width',
                         'petal_length',
                         'species']
    measurement_names = ['sepal_width',
                          'sepal_length',
                          'petal_width',
                          'petal_length']
    
    for species_name in set(iris_data['species']):
        iris_subset = iris_data[iris_data['species'] == species_name]
        plt.scatter(iris_subset['petal_length'], 
                    iris_subset['petal_width'], 
                    label=species_name, 
                    s=5, alpha=.5)
    plt.legend()
    plt.xlabel('petal_length')
    plt.ylabel('petal_width')
    plt.show()
    plt.savefig('iris_scatter.png')        

    iris = pd.read_csv(args.file_name)
    
    iris.columns = ['sepal_width',
                    'sepal_length',
                    'petal_width',
                    'petal_length',
                    'species']
    measurement_names = ['sepal_width',
                         'sepal_length',
                         'petal_width',
                         'petal_length']
    
    fig, axes = plt.subplots(2,2)
    fig.set_size_inches(10,10)
    fig.delaxes(axes[0,1])
    
    for species_name in set(iris['species']):
        iris_subset = iris[iris['species'] == species_name]
        axes[1,0].scatter(iris_subset['petal_length'], 
                          iris_subset['petal_width'], 
                          label=species_name, 
                           s=5, alpha=.5)
        axes[1,0].legend()
        axes[1,0].set_xlabel('petal_length')
        axes[1,0].set_ylabel('petal_width')
        
        axes[1,1].boxplot(iris[measurement_names],labels=measurement_names)
        axes[1,1].set_ylabel('cm')
        plt.show()
        plt.savefig('combined_plot.png')

    
if __name__ == '__main__':
    main()