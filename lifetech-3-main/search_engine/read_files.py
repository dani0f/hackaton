import os
import pdfplumber
import docx2txt

def pdf_to_text(filename):
  text = ""
  with pdfplumber.open(filename) as temp:
    for p in temp.pages:
      text = text + p.extract_text()
  return text

def doc_to_text(filename):
    my_text = docx2txt.process(filename)
    return my_text

def read_files(dir):
    document_path = dir
    dir_list = os.listdir(document_path)
    documents = []
    for file in dir_list:
        print("read: ", document_path + "/" + file)
        if(file[-3:] == "pdf"):
            documents.append("Nombre archivo: " + file + "\n" + pdf_to_text(document_path + "/" + file))
        elif(file[-3] == "ocx"):
            documents.append("Nombre archivo: " + file + "\n" + doc_to_text(document_path + "/" + file))      
    return documents

def save_files(dir_input, dir_output):
    from read_files import read_files
    documents = read_files(dir_input)
    file = dir_output
    for i in range(len(documents)):
        with open(file + f'/doc_{i}.txt', 'w', encoding='utf-8') as f:
            f.write(documents[i])


def load_files(dir):
    document_path = dir
    dir_list = os.listdir(document_path)
    documents = []
    for file in dir_list:
        print("read: ", document_path + "/" + file)
        doc = ""
        with open(document_path + '/' + file, encoding='utf-8') as f:
            lines = f.readlines()
            doc = doc + "".join(lines)
        documents.append(doc)
    return documents

#print(load_files("dataset")[0])
