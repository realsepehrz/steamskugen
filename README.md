# Steam Backup sku.sis Generator

This Python script is designed to automate the creation of a `sku.sis` file, which is essential for restoring Steam backups. It scans a specified directory for `.csd` files (chunkstore data files), calculates their sizes, and groups them by depot IDs based on file naming conventions. 

The script interacts with the user to gather additional information, such as the game name, AppID, and manifest IDs for each depot. Using this data, it generates a structured `sku.sis` file containing sections like `chunkstores`, `depots`, and `manifests`. This output file ensures that Steam can identify and verify the files during the backup restoration process.

Essentially, the script simplifies and streamlines the otherwise manual process of recreating a `sku.sis` file for Steam backups.

This script simplifies the creation of a `sku.sis` file by automating data collection and formatting.

