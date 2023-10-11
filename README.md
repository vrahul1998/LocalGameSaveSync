# LocalGameSaveSync
Used to sync Game saves stored in the home directory

# Aim
To store my game saves into a USB drive that I can plug to any system and load my saves into that system
Helps when cloud saves aren't available for certain games.

# Save
Pulls your save file from Home directory into the location where the .exe ran

# Sync
Stores the save files in the directory where the .exe is into the Home directory. If home directory already has saves, it copies it into oldSaves folder present in .exe directory

# saves.json
list of save folders you want to keep in sync. Save files are usually present within C://Users/{username}/
The above path will be added automatically to your provided path.
Provide path relative to above mentioned path
## saves.json Example
  [
      "AppData\\Local\\DeadIsland"
  ]
