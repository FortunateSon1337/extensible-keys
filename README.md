# <b>Extensible Keys</b>
## Extensible Key Format:
The Extensible Key format was designed as an alternative method for storing and password-protecting keys, largely made for personal research purposes.
## <br>File Syntax:
### All .ekf files follow this format:
[Base64-Encoded 128-Bit Salt]:[Base64-Encoded 128-Bit IV]<br>
BEGIN KEYS:<br>[Key Data]<br>END KEYS!<br>CHECKSUM: [Base64-encoded SHA256 checksum]</b><br><br>
<b>128-Bit Salt:</b><br>
This randomly generated salt is SHA256 hashed with your password to create an AES256 key which is used both for checksum validation, and encrypting/decrypting keys.<br><br>
<b>128-Bit IV:</b><br>
The randomly generated Initilization Vector to encrypt/decrypt keys in AES CBC Mode<br><br>
<b>Key Data:</b><br>
Keys are stored in a relational database with titles (i.e., "RSA PUB", "THE VAULT*") The titles are largely arbitrary with two notes: <br>1) No colons are allowed as this would break the formatting of the file<br>
2) Titles for encrypted keys must end with an asterisk, as this tells the parser to encrypt/decrypt the associated  key before saving/returning them.<br>
Each new line in the file between "START KEYS:" and "STOP KEYS!" is counted as seperate entry in the key database, the proper syntax for one of these entries is as follows:
<b>[Key Title]: [Base64-Encoded (possibly encrypted) Key][*]</b>
<br><br>
<b>SHA256 Checksum:</b>
This SHA256 hash is created by hashing all of the keys together, and the  encrypting the resulting bytes. This checksum is checked when reading an .ekf file, by generating the same hash, and instead of decrypting the original, the newly generated hash is encrypted instead, this simultaneously autheticates the password, and verifies the integrity of the stored keys<br><br><br>

## API:
This repository includes a python modue entitled "ExtensibleKeys.py" this should be considered the reference implementation. This module includes four functions:

<br><b>write_file(file_name: str, keys: dict, pw: str):</b><br>
Creates .ekf files given the desired file path and name, dictionary of keys, and and a password. The dictionary is in this format: {title(str): key(bytes)}. The password will be utf-8 encoded. Using the name of a prexisting file will raise an error to prevent accidental overwriting.<br>
<br><b>read_file(file_name: str, pw: str) -> dict:</b><br>
Reads .ekf files, given a file name and password, raises a DecryptionError if the password is incorrect or if the checksum can't be passed.<br>
<br><b> append_keys(file_name: str, new_keys: dict, pw: str):</b><br>
 Appends keys to a file, performs exactly like write_file except for that it appends to an existing file as opposed to creating one.<br>
 <br> <b>delete_keys(file_name: str, target_keys: tuple, pw: str):</b><br>
 Will remove specified keys from a file. Raises a ValueError if a non-existant key is passed.

# Security considerations and other notes:
Implement standard password requirements for protecting these files. <br><br>
As with any other password, randomized passwords should be  implemented if possible<br><br>
The same error being used for any time decryption fails is intentional, as it prevents Padding Orace attacks. All future implementations should provide simmilar ambiguity in such cases.<br><br>
It's advisable to name your keys in such a way that makes their function non-obvious, ideally slowing down any attacker that may manage to gain access to the password for a large file<br><br>
These files are suceptible to brute-force attacks, so it's still <b>strongly</b> recomended to not publicize files with sensitive keys, even if they are encrypted.<br><br>
One could make an implementation of this file format where accessing a file with no encrypted keys (i.e., a list of PGP public keys) doesn't require a password, however this could be considered a security risk as the password is also used to validate the authenticity of the stored keys.






