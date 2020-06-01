# passwordHacked

Using the API from https://haveibeenpwned.com/, this python code can be run in your local machine to check if the password you're using has ever been hacked

The protect your password and anominity the API uses a technique called k-Anonymity. The code converts your password into SHA-1 Hash and sends the first 5 characers to the API which returns all the hashed passwords that contains the same 5 characters.

The code checks then with the returned passwords to see if it matches your password and how many times it has beeen found. This way your password never leaves your local machine

To learn more check out: https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/
