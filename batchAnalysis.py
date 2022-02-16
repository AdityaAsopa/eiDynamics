import os
import sys
import pathlib
import argparse
import importlib
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from os import devnull

import analysis
from eidynamics.plot_maker  import dataframe_to_plots
from eidynamics             import ephys_classes


def batch_analysis(cellDirectory, add_cell_to_database=False, export_training_set=False, save_plots=False):
    _,savedCellFile = analysis.analyse_cell(cellDirectory,
                                        load_cell=True,
                                        save_pickle=True,
                                        add_cell_to_database = add_cell_to_database,
                                        export_training_set = export_training_set,
                                        save_plots = save_plots)

    return savedCellFile

def batch_plot(cellFile):
    try:
        dataframe_to_plots(cellFile, ploty="PeakRes",  gridRow="NumSquares", plotby="EI",        clipSpikes=True)
        dataframe_to_plots(cellFile, ploty="PeakRes",  gridRow="NumSquares", plotby="PatternID", clipSpikes=True)
        dataframe_to_plots(cellFile, ploty="PeakRes",  gridRow="PatternID",  plotby="Repeat",    clipSpikes=True)

        dataframe_to_plots(cellFile, ploty="PeakTime", gridRow="NumSquares", plotby="EI",        clipSpikes=True)
        dataframe_to_plots(cellFile, ploty="PeakTime", gridRow="NumSquares", plotby="PatternID", clipSpikes=True)
        dataframe_to_plots(cellFile, ploty="PeakTime", gridRow="PatternID",  plotby="Repeat",    clipSpikes=True)

        dataframe_to_plots(cellFile, ploty="AUC",      gridRow="NumSquares", plotby="EI",        clipSpikes=True)
        dataframe_to_plots(cellFile, ploty="AUC",      gridRow="NumSquares", plotby="PatternID", clipSpikes=True)
        dataframe_to_plots(cellFile, ploty="AUC",      gridRow="PatternID",  plotby="Repeat",    clipSpikes=True)
    except:
        pass

def meta_analysis(cellFile):
    pass

def meta_plot(allCellsFile):
    pass

def main(args):    
    all_cells_filename = pathlib.Path(args.file).stem
    all_cells_filepath = pathlib.Path(args.file)
    cell_list = importlib.import_module(all_cells_filename, all_cells_filepath)
    if args.analyse:
        all_cells = cell_list.all_cells
        project_path_root = cell_list.project_path_root
        print("Analysing all catalogued cells recordings...")
        for cellDirectory in all_cells:
                savedCellFile = batch_analysis((project_path_root / cellDirectory),add_cell_to_database=True, export_training_set=True, save_plots=True)
                print("Data saved in cell file: ",savedCellFile)


    elif args.test:
        test_cells = cell_list.test_cells
        print("Checking if analysis pipeline is working...")
        for cellDirectory in test_cells:
                savedCellFile = batch_analysis(cellDirectory,add_cell_to_database=False, export_training_set=True, save_plots=True)
                print(savedCellFile)
        print('All Tests Passed!')

    else:
        all_cells = cell_list.all_cells
        project_path_root = cell_list.project_path_root
        for cellDirectory in all_cells:
            try:
                print("Looking for analysed cell pickles to plot directly from...")
                cf = [os.path.join(cellDirectory, pickleFile) for pickleFile in os.listdir(cellDirectory) if pickleFile.endswith("cell.pkl")]
                print("Plotting from: ",cf[0])
                batch_plot(cf[0])
            except FileNotFoundError:
                print("Cell pickle not found. Beginning analysis.")
                savedCellFile = batch_analysis((project_path_root / cellDirectory),add_cell_to_database=True, export_training_set=True, save_plots=True)
                print("Data saved in cell file: ",savedCellFile)
                batch_plot(savedCellFile)

"""Argument Parser"""

parser = argparse.ArgumentParser(description="Run the main analysis program on a list of cells.")

parser.add_argument("file",   help="Required, python file that has list of selected cells to run batch analysis")

parser.add_argument( "-v", "--verbose",action="store_true")

group  = parser.add_mutually_exclusive_group()
group.add_argument("-t", "--test",    action="store_true", help="Flag to run a code test")
group.add_argument("-a", "--analyse", action="store_true", help="Flas to run batch analysis")

parser.add_argument("-p", "--plot",    action="store_true", help="to display plots")

args = parser.parse_args()

# to suppress the print statements, if verbose flag == False                
@contextmanager 
def suppress_stdout_stderr():
    """A context manager that redirects stdout and stderr to devnull"""
    with open(devnull, 'w') as fnull:
        with redirect_stderr(fnull) as err, redirect_stdout(fnull) as out:
            yield (err, out)

if args.verbose:
    main(args)
else:
    with suppress_stdout_stderr():
        main(args)

print('All Done!')


