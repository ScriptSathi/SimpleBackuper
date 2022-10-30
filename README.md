# Python script that pull backup from ssh and store is in the local filesystem

## Setup the configuration as you want

```
# ------------------------------------------
# Configuration du serveur
# ------------------------------------------
remoteUser: XXX
remoteIP: XXX # format(127.0.0.1 or somewhere.to.go.com)
remotePort: 22
sshKeyPath: '/home/sathi/.ssh/key'

# ------------------------------------------
# Configuration des backups
# ------------------------------------------
pathToBackupDir: "/somewhere/backups"
pathWhereToSaveBackup: "/folder/where/backups/are/saved"
directoryNameToBackup:
  - "folder1"
  - "folder2"

# -------------------------------------------
# Configuration de la récurence des backups
# -------------------------------------------
numberOfBackupToKeep: 3
```

**Rename the file `config.yml.example` to `config.yml` after you changed the values**

## Start the tool

```
python3 main.py
```