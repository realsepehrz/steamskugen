# Steam Backup sku.sis Generator

This Python script automates the creation of a `sku.sis` file for Steam backups by analyzing a directory containing `.csd` files. It gathers necessary information such as file sizes, depot IDs, and manifest IDs, and organizes this data into a structured format to recreate the `sku.sis` file.

---

## **Overview of Functionality**

The script performs the following tasks:
1. Identifies all `.csd` files in a specified directory.
2. Calculates the sizes of these `.csd` files.
3. Groups the files by depot IDs (based on filename conventions).
4. Prompts the user to input additional information such as the game name, AppID, and manifest IDs for each depot.
5. Generates a structured `sku.sis` file containing the gathered data.

---

## **Functions Explained**

### **1. `get_csd_files(folder_path)`**
- **Purpose**: Retrieves a list of `.csd` files from a specified directory.
- **Parameters**: 
  - `folder_path`: Path to the directory containing `.csd` files.
- **Returns**: 
  - A list of `.csd` filenames present in the directory.

### **2. `get_file_size(file_path)`**
- **Purpose**: Determines the size of a specified file in bytes.
- **Parameters**: 
  - `file_path`: Path to the file.
- **Returns**: 
  - Size of the file in bytes.

### **3. `generate_chunkstores_structure(folder_path, output_file)`**
- **Purpose**: Generates the `chunkstores` section and other necessary components of the `sku.sis` file.
- **Steps**:
  - Validates the provided folder path.
  - Calls `get_csd_files()` to fetch `.csd` files and `get_file_size()` to determine their sizes.
  - Groups files by depot IDs extracted from filenames.
  - Prompts the user to input:
    - The game name.
    - The game’s AppID.
    - Manifest IDs for each depot.
  - Constructs the `sku.sis` file structure and writes it to the specified output file.

### **4. `main()`**
- **Purpose**: Handles user input for the folder path and initiates the process to generate the `sku.sis` file.
- **Steps**:
  - Prompts the user to specify the directory containing the game’s backup files.
  - Calls `generate_chunkstores_structure()` to perform the core functionality.

---

## **Usage Instructions**

### **1. Setup**
- Place this script in a location accessible from your terminal or command prompt.
- Ensure the directory containing the `.csd` files is prepared and accessible.

### **2. Execution**
1. Run the script:
   ```bash
   python script_name.py
   ```
2. Enter the path to the directory containing `.csd` files when prompted.
3. Follow the prompts to input:
   - The game name.
   - The AppID of the game.
   - Manifest IDs for each depot.

### **3. Output**
- The script generates a `sku.sis` file in the same directory as the script. This file contains the necessary data for restoring a Steam backup.

---

## **Example Workflow**

- **Input Directory**: `C:\SteamBackups\HuntShowdown`
- **Detected Files**:
  ```
  594651_depotcache_1.csd
  594652_depotcache_1.csd
  ```
- **Generated `chunkstores` Section**:
  ```json
  "chunkstores"
  {
      "594651"
      {
          "1"       "215568035"
      }
      "594652"
      {
          "1"       "1042348268"
      }
  }
  ```

---

## **Error Handling**

- **Invalid Folder Path**: Prompts the user to re-enter the directory.
- **Missing `.csd` Files**: Alerts the user and exits the script.
- **File Size Errors**: Logs the error and assigns a size of `0` bytes to the affected file.

---

This script simplifies the creation of a `sku.sis` file by automating data collection and formatting.
