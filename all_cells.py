from pathlib import Path
import os
import sys

# These cells have been passed through the data parsing pipeline by 6 Jan 2022
all_cells =["Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\23-12-28_GrikAA404\\4041\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\23-12-04_GrikAA390\\3902\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\23-12-01_GrikAA395\\3951\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\23-12-04_GrikAA390\\3901\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\23-11-24_GrikAA375\\3751\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\23-08-10_GrikAA361\\3611\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\23-06-06_GrikAA316\\3161\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\23-06-07_GikeAA313\\3131\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\23-05-23_GrikAA310\\3101\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\23-02-13_GrikAA265\\2651\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\23-02-10_GrikAA268\\2681\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\23-02-10_GrikAA268\\2682\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\23-02-08_GrikAA282\\2821\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\23-02-08_GrikAA282\\2822\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\22-12-16_GrikAA198\\1981\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\22-11-07_GrikAA191\\1911\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\22-11-02_GrikAA193\\1931\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\22-10-21_GrikAA194\\1941\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\22-10-13_GrikAA149\\1491\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\22-10-05_GrikAA154\\1541\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\22-10-04_GrikAA152\\1524\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\22-10-04_GrikAA152\\1523\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\22-10-04_GrikAA152\\1522\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\22-10-03_GrikAA153\\1531\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\22-09-20_GrikAA162\\1621\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\22-08-17_GrikAA052\\521\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\22-06-01_GrikAA011\\111\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\22-04-18_G749\\7492\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\22-04-18_G749\\7491\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-12-31_G620\\6201\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-12-28_G630\\6301\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-12-16_G550\\5501\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-12-16_G550\\5502\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-12-15_G562\\5621\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-11-10_G561\\5611\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-09-23_G529\\5291\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-09-07_G521\\5212\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-09-07_G521\\5211\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-07-29_G388\\3881\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-07-29_G388\\3882\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-07-30_G387\\3872\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-07-30_G387\\3871\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-08-11_G379\\3791\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-08-10_G378\\3781\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-07-09_G353\\3531\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-06-04_G340\\3402\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-06-04_G340\\3401\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-06-09_G337\\3373\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-05-18_G320\\3201\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-05-12_G319\\3192\\",            
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-04-16_G294\\2941\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-04-01_G251\\2511\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-04-02_G250\\2501\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-03-06_G234\\2341\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-03-06_G234\\2342\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\21-03-04_G233\\2331\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\23-12-12_GrikAA400\\4001\\",
            "Lab\\Projects\\EI_Dynamics\\Data\\screened_cells\\23-12-25_GrikAA402\\4021\\",]

#"Lab\\Projects\\EI_Dynamics\\Data\\22-06-03_GrikAA014\\141\\",
test_cells = [".\\testExamples\\testCells\\1981\\",
              ".\\testExamples\\testCells\\5211\\",
              ".\\testExamples\\testCells\\3882\\",
              ".\\testExamples\\testCells\\111\\"]

all_cells_response_file = "Lab\\Projects\\EI_Dynamics\\AnalysisFiles\\allCells.xlsx"

##############################################################################
NCBS_data_path  = Path( r"\\storage.ncbs.res.in\adityaa\\" )
myPC_data_path = Path( "C:\\Users\\adity\\OneDrive\\NCBS\\" )
rig_data_path   = Path( "C:\\Users\\aditya\\OneDrive\\NCBS\\" )
laddu_data_path = Path( "D:\\\Aditya\\")
xutuli_data_path = Path( "/home1/bhalla/adityaa/")
test_data_path  = Path( '.\\' )

# preference of analysis path: myPC > laddu > NCBS > rig

if myPC_data_path.exists():
    project_path_root = myPC_data_path
elif laddu_data_path.exists():
    project_path_root = laddu_data_path
elif NCBS_data_path.exists():
    project_path_root = NCBS_data_path
elif rig_data_path.exists():
    project_path_root = rig_data_path
elif xutuli_data_path.exists():
    project_path_root = xutuli_data_path
else:
    print('Data path error. Testing code on test cells.')
    raise FileNotFoundError

print('>> Working on: ', project_path_root)

'''
All cells
Animal  	 CA3  	 CA1  	 Field  	 others 
23-11-24_GrikAA375  	 0  	 0  	 1	 
23-12-01_GrikAA395  	 0  	 0  	 1	 
23-12-04_GrikAA390  	 1  	 0  	 1	 
23-12-12_GrikAA400  	 0  	 0  	 1  	 SpikeTrainField
23-12-25_GrikAA402  	 1  	 0  	 1	 
23-12-28_GrikAA404  	 0  	 1  	 1	  

'''