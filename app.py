from src.data_loader import load_all_documents

if __name__=="__main__":
    doc=load_all_documents("data")
    print(doc)