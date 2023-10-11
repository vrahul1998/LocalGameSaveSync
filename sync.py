import shutil
import json
jsonFile = "saves.json"
gameSaveFolder = "gameSaves"
previousSaveFolder = "oldSave"
user_profile_folder = os.path.expanduser('~')

if __name__ == "__main__":
    if os.path.exists(jsonFile):
        with open(jsonFile, 'r') as json_file:
            # Load the JSON data from the file
            jsonList = json.load(json_file)
        if not os.path.exists(gameSaveFolder):
            os.mkdir(gameSaveFolder)
        else:
            print("gameSaves already exists")
        if os.path.exists(previousSaveFolder):
            shutil.rmtree(previousSaveFolder)
        os.mkdir(previousSaveFolder)
        for path in jsonList:
            # Use shutil.copytree() to recursively copy the source directory to the destination
            try:
                sourceDir = os.path.join(gameSaveFolder,os.path.split(path)[1])
                if os.path.exists(sourceDir):
                    destinationDir = os.path.join(user_profile_folder, path)
                    if os.path.exists(destinationDir):
                        print(f"copying into {previousSaveFolder}")
                        shutil.copytree(destinationDir, os.path.join(previousSaveFolder,os.path.split(path)[1]))
                        print(f"Deleting {destinationDir}")
                        shutil.rmtree(destinationDir)
                    shutil.copytree(sourceDir, destinationDir)
                    print(f"Folder '{sourceDir}' copied to '{destinationDir}' successfully.")
                else:
                    print(f"{sourceDir} not found in {gameSaveFolder}")
            except shutil.Error as e:
                print(f"Error: {e}")
            except OSError as e:
                print(f"Error: {e}")
    else:
        with open(jsonFile, 'w') as json_file:
            json.dump([], json_file, indent=4) 
    