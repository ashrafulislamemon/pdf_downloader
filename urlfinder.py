import os

folder_path = "issuetracker/89"  # Replace this with the actual path to the directory


arr=[]

if os.path.exists(folder_path) and os.path.isdir(folder_path):
    file_names = os.listdir(folder_path)
    print("List of file names in the directory:")
    for file_name in file_names:
        arr.append(f"http://115.127.88.45/{folder_path}/{file_name}")
      



else:
    print(f"Directory '{folder_path}' does not exist.")



# print(arr)

import json


new_arr=json.dumps(arr)

print(new_arr)