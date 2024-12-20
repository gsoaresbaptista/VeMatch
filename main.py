# import re
# import os
# import yaml
# import requests
# import zipfile
# import io
# from tqdm import tqdm


# DEFAULT_DATASETS_PATH = os.path.expanduser("~/.deep-match")

# def download_dataset(dataset_name, download_url, default_path=DEFAULT_DATASETS_PATH):
#     os.makedirs(default_path, exist_ok=True)
#     dataset_path = os.path.join(default_path, dataset_name)

#     if os.path.exists(dataset_path):
#         return dataset_path

#     file_path = f'{dataset_path}.zip'
#     print(f"Downloading '{dataset_name}'...")
#     response = requests.get(download_url, stream=True)
#     total_size = int(response.headers.get("content-length", 0))
#     block_size = 1024

#     with tqdm(total=total_size, unit="B", unit_scale=True) as progress_bar:
#         with open(file_path, "wb") as file:
#             for data in response.iter_content(block_size):
#                 progress_bar.update(len(data))
#                 file.write(data)

#     print(f"Extracting '{dataset_name}'...")

#     with zipfile.ZipFile(file_path) as zip_ref:
#         zip_ref.extractall(path=dataset_path)
#     print(f"Extracted to {dataset_path}.")

#     os.remove(file_path)

#     return dataset_path

# root = "/media/Arquivos/general/datasets/Market-1501"
# # raise NotImplementedError('Extraction method not yet implemented!')

# with open("datasets.yaml", "r") as file:
#     config = yaml.safe_load(file)
# method = config["CARLA"]["label-extraction"]["method"]

# filename = "0001_c1s1_001051_00.jpg"
# filename = "20220710182406_27_12.jpg"

# if method == "regex":
#     pattern = config["CARLA"]["label-extraction"]["pattern"]
#     match = re.match(pattern, filename)
#     label = int(match.group(1))
#     print(label)


# path = download_dataset('Market-1501', config['Market-1501']['url'])
# print(path)
