![Logo for CRISpy. Two snakes form a double helix to act as the S in the title, and nucleic acid pairs finish the visual.](/crispy_logo_RL.jpg)

# prettyCRIS.py

prettyCRIS.py was made with the aim to create a user-friendly interface for the CRIS.py analysis program. To run the user-friendly interface (known as a "GUI"), you must open an instance of terminal or command prompt in the folder containing prettyCRISpy.py and your joined .fastq files. If you would like to run the program on example data, the example data provided in the original GitHub repository (as well as in this fork) will work nicely. The nucleic acid sequences and sample/test list IDs may be easily copied over into the program and I tried to make the labels self-explanatory.

## Testing prettyCRISpy with the example data

![Screenshot of prettyCRISpy](/prettyCRISpy_screenshot.png)
Before running the example analysis, copy the fastq files into the same folder as prettyCRISpy.py, then run the prettyCRISpy.py file.

Code in the example python scripts will be copied into the program as shown below (Input Label is in the comment/after the # symbol):

```python
ID = '...' # Paste this name into the prettyCRISpy window as the "ID"
ref_seq = str.upper('...') # "Reference Sequence"
seq_start = str.upper('...') # "Sequence Start
seq_end = str.upper('...') # "Sequence End"
fastq_files = '*.fastq' # This will not have to be changed in the program if the joined fastq files are in the same folder as the prettyCRISpy.py file
test_list = [
  # For the test list, paste the text in the first set of parentheses in the "ID" box in the Test List section.
  # Paste the sequence (in the second set of parentheses) in the Test List "Seq" box.
  # Press the "Add" button.
  # Repeat for each member of the Test List (each on separate lines).
            str('...'),   str.upper('...'),
            str('...'),   str.upper('...'),
            ]
```

If you have any questions about CRISpy, I urge you to reach out to Drs. Shondra Miller and Patrick Connelly in the CAGE Lab at St. Jude. If you have questions specifically about prettyCRISpy, feel free to reach out to me.

Thank you for your interest in prettyCRISpy! I hope you find value in it.

Kindly,
Jake Steele

# CRIS.py

   Analyze NGS data for CRISPR (or any engineered endonuclease) activity and screen for clones.
   Screen for NHEJ or multiple HDR events concurrently.

CRIS.py is a an easy to use python script which analyzes NGS data for user-defined sequences.  Users directly modify the python script and run the script in the directory containing target fastq files.  After running CRIS.py, a folder is created in the current directory containing the analysis.

## Installation and Requirements

CRIS.py requires **Python 2.7** and the **Pandas library**.  (see the -py3 file to run the script using Python 3)
An easy method to install Python 2.7 and Pandas is through:
    Enthough Canopy available at: https://store.enthought.com/downloads/
    or Anaconda at https://www.anaconda.com/download/

## Usage

To use CRIS.py, directly modify the file CRIS.py in the Python editor.
Change text between quote (') marks to reflect your target amplicon.  CRIS.py reads DNA as a simple text sequence.  Therefore all DNA sequences entered must be on the same strand.
Parameters to modify are:

  1. ID:   The name of the project, gRNA or gene.  This will be used to create the output folder.
  2. ref_seq: This is the expected amplicon.  If using forward or merged reads, it will be the 'top' sequence.
  3. seq_start: A unique 12-20bp sequence in your ref_seq amplicon.  Must be **5'** of the gRNA sequence
  4. seq_end:  A unique 12-20bp sequence in your ref_seq amplicon.  Must be **3'** of the gRNA sequence.
  5. fastq_files: These are the fastq files to search.  If you want to run on all fastq files in a directory, leave as "\*.fastq".  If running on only foward reads, use nomenclature of forward reads, ie \*R1_001.fastq
  6. test_list: A series of names and sequences you wish to search for in fastq file.  Edit the name (ie g10) and the sequence for each desired test.  You can copy the line and add as many as you like.
  
![Screenshot of a PCR amplicon in Snapgene with features annotated that are useful for CRISpy, including the reference sequence, seq_start, seq_end, and three members of the Test List.](/CRISpy_example_1.jpg)

Save the program/ parameters.

Run the program. Run -> Run File
                 or click the Green triangle/play button.

Check the printed 'Working directory' and verify that is where your fastq files are located.

Check results in newly created folder that has the same label as "ID".

## Output

A folder is created in the working directory with the name 'ID' from step 1.
In the folder are two files:  

1. a CSV file:  Summary of all fastq files with test_sequences and top indels.
2. a TXT file:  Summary of all fastq files with sequence information of exact top reads from each fastq file.

## Sample files

All data from paper are uploaded in [example_directory](https://github.com/patrickc01/CRIS.py/tree/master/example_data).  In each zip file are the fastq files and CRIS.py script used to analyze the NGS data.

## Tips

1. Formatting is important.  Check that all entered text is surrounded by quotes 'like this'
2. When analyzing data from the CSV file, first look at the SNP check and raw_wt_counter to verify you are getting all reads.
3. You must close the .CSV file before running the script again.  CRIS.py can not edit a file that is already open in excel.
4. To reduce sequencing error and background indels, you may move the seq_start and seq_end closer to the test_sequences.  Of note, reducing the size of the region can result in the mssing large deletions (be sure to look at SNP_check and raw_wt_counter, values should be ~1).
5. If you are not getting any reads, double check CRIS.py is running in the correct directory.  Look at the "working directory" line and verify it is where your files are located.  If CRIS.py appears to be running in a different directory, right click the bottom window (where results show) and click "Change working directory", select the directory where your NGS reads are located.  (Canopy editor was most likely running in the folder where you originally saved CRIS.py script).

## Citing

Connelly J., Pruett-Miller S. CRIS.py: A Versatile and High-throughput Analysis Program for CRISPR-based Genome Editing. Scientific Reports 9, 4194 (2019)

## Acknowledgements

We thank Cherise Guess for scientific editing and Matthew Porteus for helpful comments on the manuscript.  We also thank the Genome Sequencing Facility of the Hartwell Center for Bioinformatics and Biotechnology at St. Jude Children’s Research Hospital.  
