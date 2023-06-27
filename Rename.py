import os
import pandas as pd

# Specify the directory containing the .mp4 files
video_directory = '/home/fade_leaf/Videos/youtube/'

# Specify the path to the CSV file with the renaming data
csv_file = '/home/fade_leaf/Downloads/Youtube ideas - Sheet1(1).csv'

def rename_videos_from_csv(directory, csv_path):
    try:
        # Load the CSV data
        df = pd.read_csv(csv_path)
        mapping = df.set_index('No.')['Question'].to_dict()

        # Rename the .mp4 files
        files = os.listdir(directory)

        for file in files:
            if file.endswith('.mp4'):
                file_path = os.path.join(directory, file)
                file_number = int(os.path.splitext(file)[0])
                new_name = mapping.get(file_number)

                if new_name:
                    new_file_path = os.path.join(directory, new_name + '.mp4')
                    os.rename(file_path, new_file_path)
                    print(f'Renamed {file} to {new_name}.mp4')

    except FileNotFoundError:
        print(f'CSV file not found: {csv_path}')

# Call the function to rename the videos
rename_videos_from_csv(video_directory.rstrip('/'), csv_file)

