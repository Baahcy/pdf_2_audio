from tkinter import Tk
from tkinter.filedialog import askopenfilename
import PyPDF2
from gtts import gTTS

Tk().withdraw()
filelocation = askopenfilename()

pdfFileObj = open(filelocation, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
page = pdfReader.getPage(0)
page_content = page.extractText()

final_file = gTTS(text=page_content, lang='en')
final_file.save('Generated Speech.mp3')
