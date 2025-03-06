### **Guide to Recreating a `sku.sis` File for Steam Backups**

This document provides a step-by-step guide to recreating a `sku.sis` file for Steam backups. The `sku.sis` file is a manifest that tells Steam which files and chunks are part of the backup. If your backup is incomplete or the `sku.sis` file is missing or incorrect, you can recreate it using this guide.

---

### **Prerequisites**
1. **Backup Files**:
   - Ensure you have all the `.csd` (chunkstore data) and `.csm` (chunkstore metadata) files for your backup.
   - Note the sizes of each `.csd` file in bytes.

2. **Manifest IDs**:
   - Obtain the correct manifest IDs for each depot. These can be found on [SteamDB](https://steamdb.info/) by searching for the game and checking the depots for the specific update version your backup corresponds to.

3. **Text Editor**:
   - Use a text editor like Notepad (Windows) or TextEdit (macOS) to create and edit the `sku.sis` file.

---

### **Step 1: Gather Information**
1. **Identify the Game and AppID**:
   - Find the AppID of the game (e.g., `594650` for "Hunt: Showdown").
   - This information is available on SteamDB or in the Steam client.

2. **List Depots**:
   - Identify all depots included in the backup. For example:
     - `594651`
     - `594652`
     - `594653`
     - `594654`

3. **Find Manifest IDs**:
   - Go to [SteamDB](https://steamdb.info/) and search for the game.
   - Navigate to the **Depots** section and find the manifest IDs for each depot corresponding to the update version of your backup.

4. **Record Chunkstore Sizes**:
   - For each `.csd` file, note its size in bytes. For example:
     - `594651_depotcache_1.csd`: `215568035` bytes
     - `594652_depotcache_1.csd`: `1042348268` bytes
     - ...

---

### **Step 2: Create the `sku.sis` File**
1. **Open a Text Editor**:
   - Open a text editor like Notepad or TextEdit.

2. **Copy the Template**:
   - Use the following template as a starting point:

```json
"sku"
{
	"name"		"Game Name"
	"disks"		"1"
	"disk"		"1"
	"backup"		"1"
	"contenttype"		"3"
	"apps"
	{
		"0"		"AppID"
	}
	"depots"
	{
		"0"		"Depot1ID"
		"1"		"Depot2ID"
	}
	"manifests"
	{
		"Depot1ID"		"Manifest1ID"
		"Depot2ID"		"Manifest2ID"
	}
	"chunkstores"
	{
		"Depot1ID"
		{
			"1"		"SizeInBytes"
		}
		"Depot2ID"
		{
			"1"		"SizeInBytes"
			"2"		"SizeInBytes"
		}
	}
}
```

3. **Customize the Template**:
   - Replace placeholders with the actual values:
     - `"Game Name"`: Replace with the name of the game (e.g., `"Hunt: Showdown"`).
     - `"AppID"`: Replace with the AppID of the game (e.g., `594650`).
     - `"Depot1ID"`, `"Depot2ID"`: Replace with the depot IDs (e.g., `594651`, `594652`).
     - `"Manifest1ID"`, `"Manifest2ID"`: Replace with the manifest IDs for each depot (e.g., `5820886928194694335`, `5332689130815039708`).
     - `"SizeInBytes"`: Replace with the sizes of the `.csd` files in bytes.

4. **Add Chunkstore Sizes**:
   - For each depot, list all `.csd` files and their sizes in the `chunkstores` section. For example:

```json
"chunkstores"
{
	"594651"
	{
		"1"		"215568035"
	}
	"594652"
	{
		"1"		"1042348268"
		"2"		"1042625638"
		"3"		"1044292638"
		...
	}
}
```

---

### **Step 3: Save the `sku.sis` File**
1. **Save the File**:
   - Save the file as `sku.sis` in the same directory as your backup files (`.csd` and `.csm` files).
   - Ensure the file extension is `.sis` and not `.txt`.

2. **Verify the File**:
   - Double-check the file for accuracy, especially the manifest IDs and chunkstore sizes.

---

### **Step 4: Restore the Backup**
1. **Open Steam**:
   - Launch the Steam client.

2. **Restore the Backup**:
   - Go to **Library** > **Game Name** > **Properties** > **Local Files** > **Backup and Restore Games**.
   - Select **Restore a Previous Backup** and follow the prompts.

3. **Allow Steam to Verify Files**:
   - Steam will verify the backup files and download any missing or updated files if necessary.

---

### **Troubleshooting**
1. **Missing Files**:
   - If Steam reports missing files, ensure all `.csd` and `.csm` files are present in the backup directory.
   - Verify the sizes of the `.csd` files match those listed in the `sku.sis` file.

2. **Incorrect Manifest IDs**:
   - If Steam requires a significant download, the manifest IDs may be incorrect. Double-check the IDs on SteamDB and update the `sku.sis` file.

3. **Outdated Backup**:
   - If the backup is from an older version of the game, Steam will download updates to bring the game to the latest version.

---

### **Example `sku.sis` File**
Here’s an example `sku.sis` file for "Hunt: Showdown" based on the steps above:

```json
"sku"
{
	"name"		"Hunt: Showdown"
	"disks"		"1"
	"disk"		"1"
	"backup"		"1"
	"contenttype"		"3"
	"apps"
	{
		"0"		"594650"
	}
	"depots"
	{
		"0"		"594651"
		"1"		"594652"
	}
	"manifests"
	{
		"594651"		"5820886928194694335"
		"594652"		"5332689130815039708"
	}
	"chunkstores"
	{
		"594651"
		{
			"1"		"215568035"
		}
		"594652"
		{
			"1"		"1042348268"
			"2"		"1042625638"
			"3"		"1044292638"
			...
		}
	}
}
```

---

### **Conclusion**
By following this guide, you can recreate a `sku.sis` file for your Steam backup and restore your game with minimal additional downloads. If you encounter any issues, double-check the manifest IDs and chunkstore sizes, and ensure all backup files are present and correctly named. Let me know if you need further assistance!
