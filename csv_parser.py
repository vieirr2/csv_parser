import matplotlib.pyplot as plt
import pandas as pd
import sys
import click

@click.group() #dir of functions 
def cli():
    """Can display and plot csv files."""
    pass

@cli.command()
@click.argument('filename')
def display(filename):
    """Displays the column names and their data types."""
    df = pd.read_csv(filename)
    print(df.dtypes)
    
@cli.command()
@click.argument('filename')
@click.option('--column', default=None, help= 'Name of column to plot. If not used, will be plotted')
def plot(filename):
    """Plots a histogram of a column of the cvs file."""
    df = pd.read_csv(filename)
    if column is None:
        df.hist()
    else:
        df[column].hist()
        plt.title(column)
        plt.ylabel('frequency')
    plt.show()

if __name__ == '__main__':
    cli()