# <b>Extensible Keys</b>
## Extensible Key Format:
### The extensible key format was designed to serve as an alternative to .PEM with a (slightly) less verbose syntax and more importantly, built in password protection and authetification of your keys.
## <br>File Syntax:
### All .ekf files follow this format:
### <b>[Base64-Encoded 128-Bit Salt]:[Base64-Encoded 128-Bit IV]<br>
### BEGIN KEYS:<br>[Key Data]<br>END KEYS!<br>CHECKSUM: [Base64-encoded SHA256 checksum]</b><br><br>
### <b>128-Bit Salt:</b>
### This randomly generated salt is SHA256 hashed with your password to create an AES256 key which is used both for checksum validation, and encrypting/decrypting keys.<br><br>
### <b>128-Bit IV:</b>
### The randomly generated Initilization Vector to encrypt/decrypt keys in AES CBC Mode<br><br>
###
### <b>Key Data:</b>
### Keys are stored in a relational database with titles (i.e., "RSA PUB", "THE VAULT*") The titles are largely arbitrary with two notes: <br><br>1) No colons are allowed as this would break the formatting of the file
### 2) Titles for encrypted keys must end with an asterisk, as this tells the parser to encrypt/decrypt the associated  key before saving/returning them.<br><br>
### Each new line in the file between "START KEYS:" and "STOP KEYS!" is counted as seperate entry in the key database, the proper syntax for one of these entries is as follows:
### <b>[Key Title]: [Base64-Encoded (possibly encrypted) Key][*]</b>

<br>

### <b>SHA256 Checksum:</b>
### This SHA256 hash is created by hashing all of the keys together, and the  encrypting the resulting bytes. This checksum is checked when reading an .ekf file, by generating the same hash, and instead of decrypting the original, the newly generated hash is encrypted instead, this simultaneously autheticates the password, and verifies the integrity of the stored keys<br><br><br>

## API:
### This repository includes a python modue entitled "ExtensibleKeys.py" this should be considered the reference implementation. This module includes four functions:

### <br><b>write_file(file_name: str, keys: dict, pw: str):</b>
### Creates .ekf files given the desired file path and name, dictionary of keys, and and a password. The dictionary is in this format: {title(str): key(bytes)}. The password will be utf-8 encoded. Using the name of a prexisting file will raise an error to prevent accidental overwriting.
### <br><b>read_file(file_name: str, pw: str) -> dict:</b>
### Reads .ekf files, given a file name and password, raises a DecryptionError if the password is incorrect or if the checksum can't be passed.
### <br><b> append_keys(file_name: str, new_keys: dict, pw: str):</b>
### Appends keys to a file, performs exactly like write_file except for that it appends to an existing file as opposed to creating one.<br><br><br>

# Security considerations and other notes:
### Implement standard password requirements for protecting these files. <br><br>
### As with any other password, randomized passwords should be  implemented if possible<br><br>
### The same error being used for any time decryption fails is intentional, as it prevents Padding Orace attacks. All future implementations should provide simmilar ambiguity in such cases.<br><br>
### It's advisable to name your keys in such a way that makes their function non-obvious, ideally slowing down any attacker that may manage to gain access to the password for a large file<br><br>
### These files are suceptible to brute-force attacks, so it's still <b>strongly</b> recomended to not publicize files with sensitive keys, even if they are encrypted.<br><br>
### One could make an implementation of this file format where accessing a file with no encrypted keys (i.e., a list of PGP public keys) doesn't require a password, however this could be considered a security risk as the password is also used to validate the authenticity of the stored keys.






