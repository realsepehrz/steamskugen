import os

def get_csd_files(folder_path):
    """
    Returns a list of.csd files in the given directory.
    """
    try:
        return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.csd')]
    except Exception as e:
        print(f"Error getting.csd files: {e}")
        return []

def get_file_size(file_path):
    """
    Returns the size of the given file.
    """
    try:
        return os.path.getsize(file_path)
    except Exception as e:
        print(f"Error getting file size: {e}")
        return 0

def generate_chunkstores_structure(folder_path, output_file):
    """
    Generates the chunkstores structure from the given folder path and writes it to the output file.
    """
    try:
        # Check if the provided path is a valid directory
        if not os.path.isdir(folder_path):
            print(f"The path '{folder_path}' is not a valid directory.")
            return

        # List all.csd files in the directory
        files = get_csd_files(folder_path)

        if not files:
            print(f"No.csd files found in the directory '{folder_path}'.")
            return

        # Create a dictionary to store chunkstores structure
        chunkstores = {}
        depots_arr = []

        for file in files:
            file_path = os.path.join(folder_path, file)
            file_size = get_file_size(file_path)
            first_part = file.split('_')[0]
            last_part = file.split('_')[-1].split('.')[0]

            if first_part not in depots_arr:
                depots_arr.append(first_part)

            if first_part not in chunkstores:
                chunkstores[first_part] = {}

            chunkstores[first_part][last_part] = str(file_size)

        # Generate the chunkstores string
        chunkstores_string = ""
        for key, value in chunkstores.items():
            chunkstores_string += f'		"{key}"\n		{{\n'
            sorted_value = dict(sorted(value.items(), key=lambda item: int(item[0])))
            for sub_key, sub_value in sorted_value.items():
                chunkstores_string += f'			"{sub_key}"\t\t"{sub_value}"\n'
            chunkstores_string +='		}\n'

        depots_string = ""
        for i in range(len(depots_arr)):
            depots_string += f'		"{i}"		"{depots_arr[i]}"\n'

        # Get game name
        gamename = folder_path.split("\\")[-1]
        print(f'Game: {gamename}')
        print("The game name should be accurate!")
        user_game_name_prompt = input(f'Enter 0 to continue or enter the game name: ')
        if user_game_name_prompt!= "0" and user_game_name_prompt!= "":
            gamename = user_game_name_prompt

        # Get game ID
        game_id = input("Enter the Game ID: ")

        # Get manifest IDs
        manifest_string = ""
        for i in depots_arr:
            manifest_id = input(f"Enter {i}'s Manifest: ")
            manifest_string += f'		"{i}"		"{manifest_id}"\n'

        print("\nGenerated chunkstores structure:")
        # Write the chunkstores string to the output file
        with open(output_file, 'w') as f:
            f.write('"SKU"\n')
            f.write('{\n')
            f.write(f'	"name"		"{gamename}"\n')
            f.write('	"disks"		"1"\n')
            f.write('	"disk"		"1"\n')
            f.write('	"backup"		"1"\n')
            f.write('	"contenttype"		"3"\n')
            f.write('	"apps"\n')
            f.write('	{\n')
            f.write(f'		"0"		"{game_id}"\n')
            f.write('	}\n')
            f.write('	"depots"\n')
            f.write('	{\n')
            f.write(depots_string)
            f.write('	}\n')
            f.write('	"manifests"\n')
            f.write('	{\n')
            f.write(manifest_string)
            f.write('	}\n')
            f.write('	"chunkstores"\n')
            f.write('	{\n')
            f.write(chunkstores_string)
            f.write('	}\n')
            f.write('}\n')

        print(f"\nChunkstores structure written to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Specify the output file
    output_file = 'sku.sis'

    while True:
        # Get the folder path from the user
        folder_path = input("Enter the game's path: ")

        # Check if the path exists and is a directory
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            break
        else:
            print("Invalid path. Please enter a valid directory path.")

    # Call the function to generate chunkstores structure
    generate_chunkstores_structure(folder_path, output_file)

if __name__ == "__main__":
    main()
