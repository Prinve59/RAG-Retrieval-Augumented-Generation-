from pathlib import Path
from typing import List,Any
from langchain_community.document_loaders import PyPDFLoader,TextLoader,CSVLoader,Docx2txtLoader,JSONLoader
from langchain_community.document_loaders.excel import UnstructuredExcelLoader

def load_all_documents(data_dir:str)->List[Any]:
    data_path=Path(data_dir).resolve()
    print(f"[DEBUG] Data Path:{data_path}")
    documents=[]
    #pdf files
    pdf_files=list(data_path.glob('**/*.pdf'))
    print(f"[DEBUG] found {len(pdf_files)} pdf files{[str(f) for f in pdf_files]}")
    for pdf_file in pdf_files:
        print(f"[DEBUG] loading pdf :{pdf_file}")
        try:
            loader=PyPDFLoader(str(pdf_file))
            loaded=loader.load()
            print(f"[DEBUG] loaded {len(loaded)} pdf docs from {pdf_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] failed to load {pdf_file}:{e}")

    #txt files
    txt_files=list(data_path.glob('**/*.txt'))
    print(f"[DEBUG] found {len(txt_files)} txt files{[str(f) for f in txt_files]}")
    for txt_file in txt_files:
        print(f"[DEBUG] loading txt :{txt_file}")
        try:
            loader=TextLoader(str(txt_file))
            loaded=loader.load()
            print(f"[DEBUG] loaded {len(loaded)} txt docs from {txt_file}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] failed to load {txt_file}:{e}")
    return documents