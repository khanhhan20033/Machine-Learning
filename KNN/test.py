import shutil
import os


def duplicate_file(source_path, destination_dir, num_copies):
    if not os.path.isfile(source_path):
        raise FileNotFoundError(f"The source file {source_path} does not exist.")
    if not os.path.isdir(destination_dir):
        os.makedirs(destination_dir)

    base_name = os.path.basename(source_path)
    name, ext = os.path.splitext(base_name)

    for i in range(1, num_copies + 1):
        destination_path = os.path.join(destination_dir, f"{name}_copy_{i}{ext}")
        shutil.copy2(source_path, destination_path)
        print(f"Created copy {i}: {destination_path}")


# Example usage:
source_file_path = "C:/Users/MAC/Downloads/quiet.mp4"  # Replace with your source file path
destination_directory = "C:/Users/MAC/Downloads/video_stop"  # Replace with your destination directory
number_of_copies = 63

duplicate_file(source_file_path, destination_directory, number_of_copies)
