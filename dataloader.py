# imports
import os
import re

import pandas as pd


def read_file_content(file_path: str) -> str:
    """
    Read and return the content of a file, stripping any leading/trailing whitespace.

    :param file_path: Path to the file to be read
    :return: Content of the file as a string
    """
    with open(file_path) as file:
        return file.read().strip()


def get_case_number(case_name: str) -> int:
    """
    Extract the case number from a case name, removing any leading zeros.

    :param case_name: Name of the case (e.g., "case-01")
    :return: Case number as an integer
    """
    return int(re.search(r"\d+", case_name).group().replace("0", ""))


def process_non_plagiarized_files(
    case_path: str, original_content: str, case_number: int
) -> list:
    """
    Process non-plagiarized files for a given case.

    :param case_path: Path to the case folder
    :param original_content: Content of the original file
    :param case_number: Number of the current case
    :return: List of dictionaries containing information about non-plagiarized files
    """
    non_plagiarized_path = os.path.join(case_path, "non-plagiarized")
    rows = []

    # Get folders, excluding hidden folders and those containing "01", "02", or "03"
    folders = [
        f
        for f in os.listdir(non_plagiarized_path)
        if not f.startswith(".") and not any(x in f for x in ["01", "02", "03"])
    ]
    for folder in folders:
        folder_path = os.path.join(non_plagiarized_path, folder)
        java_files = [f for f in os.listdir(folder_path) if f.endswith(".java")]

        for file in java_files:
            file_content = read_file_content(os.path.join(folder_path, file))
            rows.append(
                {
                    "L": 0,  # Level 0 for non-plagiarized files
                    "case": case_number,
                    "sample_1": original_content,
                    "sample_2": file_content,
                    "plagiarized": False,
                    "reason": None,
                }
            )
    return rows


def process_plagiarized_files(
    case_path: str, original_content: str, case_number: int
) -> list:
    """
    Process plagiarized files for a given case.

    :param case_path: Path to the case folder
    :param original_content: Content of the original file
    :param case_number: Number of the current case
    :return: List of dictionaries containing information about plagiarized files
    """
    plagiarized_path = os.path.join(case_path, "plagiarized")
    rows = []

    # Get plagiarized folders, excluding hidden folders
    plagiarized_folders = [
        f for f in os.listdir(plagiarized_path) if not f.startswith(".")
    ]
    for p_folder in plagiarized_folders:
        p_folder_path = os.path.join(plagiarized_path, p_folder)
        # Get level folders, excluding hidden folders and "01"
        level_folders = [
            f for f in os.listdir(p_folder_path) if not f.startswith(".")
        ]
        for level_folder in level_folders:
            level_folder_path = os.path.join(p_folder_path, level_folder)
            java_files = [
                f for f in os.listdir(level_folder_path) if f.endswith(".java")
            ]

            for file in java_files:
                if "L1/01/" in os.path.join(level_folder_path, file):
                    continue
                file_content = read_file_content(os.path.join(level_folder_path, file))
                rows.append(
                    {
                        "L": int(level_folder.replace("L", "")),  # Extract level number
                        "case": case_number,
                        "sample_1": original_content,
                        "sample_2": file_content,
                        "plagiarized": True,
                        "reason": None,
                    }
                )
    return rows


def build_eval_dataset(data_path: str) -> pd.DataFrame:
    """
    Build the evaluation dataset by processing all cases in the given data path.

    :param data_path: Path to the directory containing all case folders
    :return: Pandas DataFrame containing the evaluation dataset
    """
    rows = []
    # Get all case folders
    case_folders = [folder for folder in os.listdir(data_path) if "case-" in folder]

    for case in case_folders:
        case_path = os.path.join(data_path, case)
        case_number = get_case_number(case)

        # Find and read the original file
        original_file = [
            f
            for f in os.listdir(os.path.join(case_path, "original"))
            if f.endswith(".java")
        ][0]
        original_content = read_file_content(
            os.path.join(case_path, "original", original_file)
        )

        # Process non-plagiarized and plagiarized files
        rows.extend(
            process_non_plagiarized_files(case_path, original_content, case_number)
        )  
        rows.extend(process_plagiarized_files(case_path, original_content, case_number))

    return pd.DataFrame(rows)


def check_if_data_folder_exits(data_folder: str) -> None:
    # Check if the folder exists
    if not os.path.exists(data_folder):
        print(f"The folder '{data_folder}' does not exist in the repository.")
        print(
            "Please download it from: https://github.com/oscarkarnalim/sourcecodeplagiarismdataset/blob/master/IR-Plag-Dataset.zip"
        )
        print(
            "After downloading, extract the contents to the 'data' folder in your repository."
        )
        raise Exception(f"The folder '{data_folder}' does not exist.")
    else:
        print(
            f"The folder '{data_folder}' exists. You can proceed with loading the data."
        )
