import sys, os
if sys.version_info[0] == 3:
	import tkinter as tk
else:
	import Tkinter as tk
from PIL import Image, ImageTk
import glob

import CRISpy_v2 as CRISpy_v2 # Forcing import of CRISpy scripts to include in one-file EXE
import CRISpy_v1 as CRISpy_v1
from importlib import import_module # The hyphen in the py3 script messes with imports. Have to use this as workaround
CRISpy_v1_py3 = import_module('CRISpy_v1-py3')

def prettyCRISpy():
	# St Jude Colors
	SJ_RED = '#d11947'
	SJ_DGRAY = '#474c55'
	SJ_LGRAY = '#b3b3b3'
	SJ_BLUE = '#1874dc'
	prettyLabelFont = 'Verdana 10 bold'
	prettyInsideFont = 'Verdana 10'

	root = tk.Tk()

	root.minsize(720,720)
	root.title('prettyCRIS.py')

	window = tk.Frame(root, bg=SJ_DGRAY)
	window.place(relx=0, rely=0, relwidth=1, relheight=1)

	contentFrame = tk.Frame(root, bg=SJ_LGRAY)
	contentFrame.place(relx=0.0125, rely=0.025, relwidth=0.975, relheight=0.95)

	CRISpyBackgroundImage = ImageTk.PhotoImage(Image.open('crispy_logo_RL.jpg').resize((500,280), Image.ANTIALIAS))
	background_label = tk.Label(contentFrame, image=CRISpyBackgroundImage, bg='white')
	background_label.place(relx=0.0,rely=0.00,relwidth=1,height=280)

	# Container to hold all content in the contentFrame with a 5% margin on all sides
	userInputFrame = tk.Frame(contentFrame, padx=10, pady=10)
	userInputFrame.place(relx=0.05, y=300, relwidth=0.9, relheight=0.525)

	inputBoxes = 0 # Number of input boxes in userInputFrame -- Used to determine rely/spacing
	inputSpacing = 0.09 # rely per input box

	# CRISpy Version selection drop-down menu
	versionsAvailable = ['CRISpy_v2', 'CRISpy_v1-py3', 'CRISpy_v1']
	# for k in glob.glob('CRISpy*.py'):
	# 	versionsAvailable.append(os.path.splitext(k)[0]) # Fetch available CRISpy versions in current working directory
	CRISpyVersionSelected = tk.StringVar(root)
	CRISpyVersionSelected.set(versionsAvailable[0])
	label_versionDropDown = tk.Label(userInputFrame, text='CRIS.py Version:', font=prettyLabelFont, bg=SJ_LGRAY, fg='black')
	label_versionDropDown.place(relx=0, rely=(inputSpacing * inputBoxes), relwidth=0.25, height=20)
	versionDropDown = tk.OptionMenu(userInputFrame, CRISpyVersionSelected, *versionsAvailable)
	versionDropDown.place(relx=0.255, rely=(inputSpacing * inputBoxes)-0.005, relwidth=0.75, height=25)
	inputBoxes += 1

	# Labels and single-line Text entry boxes for the ID, ref sequence, seq start, and seq end
	label_userID = tk.Label(userInputFrame, text='ID:', font=prettyLabelFont, bg=SJ_LGRAY, fg='black')
	label_userID.place(relx=0, rely=(inputSpacing * inputBoxes), relwidth=0.25, height=20)
	userID = tk.Entry(userInputFrame, bg=SJ_DGRAY, fg='white')
	userID.place(relx=0.255, rely=(inputSpacing * inputBoxes), relwidth=0.745, height=20)
	inputBoxes += 1

	label_userRef_Seq = tk.Label(userInputFrame, text='Reference Sequence:', font=prettyLabelFont, bg=SJ_LGRAY, fg='black')
	label_userRef_Seq.place(relx=0, rely=(inputSpacing * inputBoxes), relwidth=0.25, height=20)
	userRef_Seq = tk.Entry(userInputFrame, bg=SJ_DGRAY, fg='white')
	userRef_Seq.place(relx=0.255, rely=(inputSpacing * inputBoxes), relwidth=0.745, height=20)
	inputBoxes += 1

	label_userSeq_Start = tk.Label(userInputFrame, text='Sequence Start:', font=prettyLabelFont, bg=SJ_LGRAY, fg='black')
	label_userSeq_Start.place(relx=0, rely=(inputSpacing * inputBoxes), relwidth=0.25, height=20)
	userSeq_Start = tk.Entry(userInputFrame, bg=SJ_DGRAY, fg='white')
	userSeq_Start.place(relx=0.255, rely=(inputSpacing * inputBoxes), relwidth=0.745, height=20)
	inputBoxes += 1

	label_userSeq_End = tk.Label(userInputFrame, text='Sequence End:', font=prettyLabelFont, bg=SJ_LGRAY, fg='black')
	label_userSeq_End.place(relx=0, rely=(inputSpacing * inputBoxes), relwidth=0.25, height=20)
	userSeq_End = tk.Entry(userInputFrame, bg=SJ_DGRAY, fg='white')
	userSeq_End.place(relx=0.255, rely=(inputSpacing * inputBoxes), relwidth=0.745, height=20)
	inputBoxes += 1

	label_fastq = tk.Label(userInputFrame, text='.fastq Nomenclature:', font=prettyLabelFont, bg=SJ_LGRAY, fg='black')
	label_fastq.place(relx=0, rely=(inputSpacing * inputBoxes), relwidth=0.25, height=20)
	fastqNomenclatureType = tk.StringVar(root)
	fastqNomenclatureType.set('SUFFIX')
	fastqNomenclatureDropdown = tk.OptionMenu(userInputFrame, fastqNomenclatureType, 'PREFIX', 'SUFFIX')
	fastqNomenclatureDropdown.place(relx=0.255, rely=(inputSpacing * inputBoxes)-0.005, relwidth=0.125, height=25)
	userfastq = tk.Entry(userInputFrame, bg=SJ_DGRAY, fg='white')
	userfastq.place(relx=0.385, rely=(inputSpacing * inputBoxes), relwidth=0.615, height=20)
	inputBoxes += 1

	# test_list implementation box
	test_list = []
	def addToTestList():
		if testListUpdateBox.get(1.0, 'end') != '': # Clear testListUpdateBox if not already empty
			testListUpdateBox.config(state='normal')
			testListUpdateBox.delete(1.0, 'end')
			testListUpdateBox.config(state='disabled')
			testListUpdateString = ''

		updateList = []
		if user_testListAddID.get() == '': # If there is no ID entered...
			testListUpdateString = 'No ID to add to test_list. Please add an ID and try again.'
			testListUpdateBox.config(state='normal')
			testListUpdateBox.insert('end', testListUpdateString)
			testListUpdateBox.config(state='disabled')
		elif user_testListAddSeq.get() == '': # If there is no seq entered...
			testListUpdateString = 'No sequence to add to test_list. Please add a sequence and try again.'
			testListUpdateBox.config(state='normal')
			testListUpdateBox.insert('end', testListUpdateString)
			testListUpdateBox.config(state='disabled')
		else:
			updateList = [str(user_testListAddID.get()), str(user_testListAddSeq.get())]
			test_list.extend(updateList)
			testListUpdateBox.config(state='normal')
			testListUpdateString = ('Added ID: ' + updateList[0] + ' Seq: ' + updateList[1]
				+ ' to test_list.\nNew test_list includes IDs:')
			for i in range(0, len(test_list), 2):
				testListUpdateString += ' ' + test_list[i]
			testListUpdateBox.insert('end', testListUpdateString)
			testListUpdateBox.config(state='disabled')
			user_testListAddID.delete(0, 'end')
			user_testListAddSeq.delete(0, 'end')

	label_testListSectionHeader = tk.Label(userInputFrame, text='Test List (optional):', font=prettyLabelFont, fg='black')
	label_testListSectionHeader.place(relx=0, rely=(inputSpacing * inputBoxes), width=150, height=20)
	label_testListAddID = tk.Label(userInputFrame, text='ID:', font=prettyLabelFont, bg=SJ_LGRAY, fg='black')
	label_testListAddID.place(relx=0, rely=(inputSpacing * inputBoxes) + 0.075, relwidth=0.1, height=20)
	user_testListAddID = tk.Entry(userInputFrame, bg=SJ_DGRAY, fg='white')
	user_testListAddID.place(relx=0.105, rely=(inputSpacing * inputBoxes) + 0.075, relwidth=0.14, height=20)
	label_testListAddSeq = tk.Label(userInputFrame, text='Seq:', font=prettyLabelFont, bg=SJ_LGRAY, fg='black')
	label_testListAddSeq.place(relx=0.25, rely=(inputSpacing * inputBoxes) + 0.075, relwidth=0.1, height=20)
	user_testListAddSeq = tk.Entry(userInputFrame, bg=SJ_DGRAY, fg='white')
	user_testListAddSeq.place(relx=0.355, rely=(inputSpacing * inputBoxes) + 0.075, relwidth=0.545, height=20)
	user_testListAdd_Button = tk.Button(userInputFrame, bg=SJ_RED, font=prettyLabelFont, fg='white', text='Add', command=addToTestList)
	user_testListAdd_Button.place(relx = 0.905, rely = (inputSpacing * inputBoxes) + 0.075, relwidth=0.095, height=20)
	inputBoxes+= 1.75
	testListUpdateBox = tk.Text(userInputFrame, height=2, width=30, bg=SJ_DGRAY, fg='white')
	testListUpdateBox.insert('end', 'test_list Status:')
	testListUpdateBox.place(relx=0, rely=inputSpacing * inputBoxes, relwidth=1, height=40)
	testListUpdateBox.config(state='disabled')
	inputBoxes += 1.75


	ID, ref_seq, seq_start, seq_end, fastq_files = ('' for j in range(5))

	
		
		
	# Submit/analyze button		
	def Analyze():
		## Default Values for testing. Uncomment and analyze will auto-fill with these values instead of fetching entered values.
		# ID = 'Locus_1'
		# ref_seq = str.upper('agggaatgccccggagggcggagaactgggacgaggccgaggtaggcgcggaggaggcaggcgtcgaagagtacggccctgaagaagacggcggggaggagtcgggcgccgaggagtccggcccggaagagtccggcccggaggaactgggcgccgaggaggagatgg')
		# seq_start = str.upper('GCGGAGAACTG')
		# seq_end = str.upper('GCCGAGGAGGA')
		# test_list = [
		# 	str('g10'),   str.upper('GAGGCAGGCGTCGAAGAGTACGG'), 
		# 	str('g14'),   str.upper('CGGCCCTGAAGAAGACGGCGGGG'),
		# 	str('g6'),   str.upper('CCGAGGAGTCCGGCCCGGAAGAG')
		# 	]

		## Fetch user-input values
		ID = str.upper(userID.get())
		ref_seq = str.upper(userRef_Seq.get())
		seq_start = str.upper(userSeq_Start.get())
		seq_end = str.upper(userSeq_End.get())
		fastq_files = ''
		if (fastqNomenclatureType.get() == 'PREFIX') :
			fastq_files = str(userfastq.get()) + '*.fastq'
		elif (fastqNomenclatureType.get() == 'SUFFIX') :
			fastq_files = '*' + str(userfastq.get()) + '.fastq'
		else :
			print('No fastqNomenclatureType.')

		vSelected = CRISpyVersionSelected.get()
		if vSelected == 'CRISpy_v2':
			fastq_files = glob.glob(fastq_files)
			print "Input files:"
			for f in fastq_files:
				print "  " + f
			CRISpy_v2.search_fastq(ID, ref_seq, seq_start, seq_end, fastq_files, test_list)
		elif vSelected == 'CRISpy_v1-py3':
			CRISpy_v1_py3.search_fastq(ID, ref_seq, seq_start, seq_end, fastq_files, test_list)
		elif vSelected == 'CRISpy_v1':
			CRISpy_v1.search_fastq(ID, ref_seq, seq_start, seq_end, fastq_files, test_list)
		
		print('Done')
		return ID,ref_seq,seq_start,seq_end,fastq_files,test_list

	analyzeButton = tk.Button(userInputFrame, bg=SJ_RED, font=prettyLabelFont, fg='white', text='Analyze & Export', command=Analyze)
	analyzeButton.place(relx=0.25, rely=inputSpacing * inputBoxes, relwidth=0.5, relheight=0.15)

	root.mainloop()

prettyCRISpy()