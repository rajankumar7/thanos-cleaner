"""Thanos cleaner"""
import os
import random
import argparse

def find_files(target_dir: str) -> list:
    try:
        file_paths = []
        for root, directories, files in os.walk(target_dir):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
    except PermissionError:
        print("Permission denied. Please provide root Permission.")
    return file_paths

def snap(user_inputs : argparse.Namespace):
    target_dir = str(user_inputs.target)
    print("Thanos is targeting", target_dir)
    target_files = find_files(target_dir=target_dir)
    print("Targetted Files:")
    for file in target_files:
        print(file)
    print("******Snapping******")
    random.shuffle(target_files)
    for i in range(0, int(len(target_files) / 2)):
        print("Deleting: ", target_files[i])
        try:
            os.remove(target_files[i])
        except PermissionError:
            print("Root permissoin needed.")
            raise PermissionError
        except Exception:
            pass
    print("********************")
    print("Half of them still live!")

