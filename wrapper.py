from data_prep.data_prep import match_summary, over_summary
from embeddings.embeddings import create_embeddings
from vector_storage.vector import vector_db_storage
import json
from pathlib import Path


if __name__ == "__main__":

    # with open("./1000851.json",'r',encoding='utf-8') as f:
    #     json_data = json.load(f)
    #     str_ = ''
    #     str_ = match_summary(json_data) + "\n" + over_summary(json_data)
    #     embeddings,input = create_embeddings(str_)
    #     vector_db_storage(embeddings,input)

    target_dir = Path("./raw_data/all_json")

    for file in target_dir.iterdir():

        if file.is_file():
            print(f"Reading file {file}")

            with open(file,'r',encoding='utf-8') as f:

                json_data = json.load(f)
                str_ = ''

                try:
                    str_ = match_summary(json_data) + "\n" + over_summary(json_data)
                    embeddings, input = create_embeddings(str_)
                    vector_db_storage(embeddings,input)
                except Exception as e:
                    print(f"Error in this file {file} Moving on...")
                    continue

    
