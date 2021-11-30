# comps-nba-roster-construction

This is my repository for my Senior Comps project.

To run these files you will need Python and a Python IDE, as well as the Python packages Numpy and Pandas downloaded and available to use. You will also need some machine learning packages such as Scikit-Learn and optionally Matplotlib, as the plots aren't crucial to the outcome of the code they're in.

To quickly install any packages you are potentially missing, you can go to this address for more instructions on how to pip install these packages through your command line:
https://packaging.python.org/tutorials/installing-packages/

The first file you will need to run is the basketballref_scrape.py file. This file will be using BeautifulSoup to web-scrape basketball stats from the website basketball-reference as well as the Stats pages of the official NBA site. At the end, it will change gather all the stats up and turn them into a csv file (csv files are spreadsheet files you can open through Excel or Numbers, etc.) on your computer. This file should run without you having to make any changes to the code.

The next file you will run is the kmeans_nba.py file. This file will be using Scikit-Learn, Kmeans-Clustering and Principal Component Analysis to do machine learning and fitting each NBA player into a role category based on numerous stats. This file will also gather these players roles and turn them into seperate csv files at the end of the code. This file should run without you having to make any changes to the code.

The third file you will run is the clean_up.py file. This file will need some editing on your end as it uses your computer path to find the csv files that the previous codes have made. 
- You will need to find the csv files : new_concat_4.csv, new_concat_4_defense.csv, and df_ff.csv in your computer. 
- After finding it, you will need to find its file path which you will most likely be able to do through right clicking on the csv file.
- Replace the file paths from the code with your new file paths, the code file paths you will be replacing are at the very beginning of the code.
- After that, you shouldn't need to make any more changes to the code.

The objective of this code is to insert percentile ranks next to each stat of our players based on the roles that they play and make new csv files with the added information.

The last file you will run is the comps_algo.py file. This file will also need some editing on your end as we will be finding the file paths for the csv files we just made with the clean_up.py file.
- You will need to find the csv files: concat_4_ranks.csv and concat_4_def_ranks.csv.
- The df_ff.csv file can use the same path you used in the clean_up.py file.
- After finding them, do the same process of figuring out the file path for the csv files and replacing the existing path in the code with yours.
- The rest of the code should work after changing the file paths.
This file isn't done yet but will be the file that implements the suggestions of NBA players for teams to possibly add to their teams.


