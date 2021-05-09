# Google Linux Machine Management Project (Replication Document)

## Connor Shields, Carlo Preciado, Facundo Muñoz, Samuel Neus

### Downloading the Code
1. Downloading the code using a ZIP file
- The final code is posted at https://github.com/Cpreciad/Data-Structures-Preternship
- Download the ZIP by clicking on the green “Code” button, and clicking the download ZIP dropdown option
- Extract the Final_Code folder from within the Python_Code subfolder, into your chosen directory.
2. Downloading the code using `curl`
- To move code to your local machine, simply curl the two necessary modules in a directory of your choice:
- From the working directory, run `curl -LO https://raw.githubusercontent.com/Cpreciad/Data-Structures-Preternship/main/Python_Code/Final_Code/main.py`
- Also run `curl -LO https://raw.githubusercontent.com/Cpreciad/Data-Structures-Preternship/main/Python_Code/Final_Code/data_collector.py`

### Running the Code
1. Navigate to the directory where you would like the data directory to reside
- You may need to set the proper permissions in order to execute the program. Run `chmod a+x main.py` in order to make the script executable.
2. To run the code, the user may run `./main.py`. By default, the program will return to stdout the formatted information for the hard drive info, the cpu info, and finally the memory info.
- The flag `-h` provides more specific information on the function of each flag and can be run like so: `./main.py -h`.
- The flags `-H`, `-C`, and `-M` may be added at runtime to remove the hard drive info, cpu info and memory info respectively.
- The flag `-d` may be run with a directory name to create a directory in which to store the data files or use an existing directory.
- The flag `-s` may be run to force the program to run silently and not output to stdout at all. This should always be run in conjunction with the `-d` flag, or else nothing will be outputted.
