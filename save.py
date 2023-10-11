import shutil
import json
gameSaveFolder = "gameSaves"
user_profile_folder = os.path.expanduser('~')
jsonFile = "saves.json"

if __name__ == "__main__":
    if os.path.exists(jsonFile):
        with open(jsonFile, 'r') as json_file:
            # Load the JSON data from the file
            jsonList = json.load(json_file)
        if not os.path.exists(gameSaveFolder):
            os.mkdir(gameSaveFolder)
        else:
            print("gameSaves already exists")

        for path in jsonList:
            # Use shutil.copytree() to recursively copy the source directory to the destination
            try:
                sourceDir = os.path.join(user_profile_folder, path)
                destinationDir = os.path.join(gameSaveFolder,os.path.split(path)[1])
                if os.path.exists(destinationDir):
                    print(f"Deleting {destinationDir}")
                    shutil.rmtree(destinationDir)
                shutil.copytree(sourceDir, destinationDir)
                print(f"Folder '{sourceDir}' copied to '{destinationDir}' successfully.")
            except shutil.Error as e:
                print(f"Error: {e}")
            except OSError as e:
                print(f"Error: {e}")
    else:
        with open(jsonFile, 'w') as json_file:
            json.dump([], json_file, indent=4) 