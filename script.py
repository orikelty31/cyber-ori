"""
Author: Ori Kelty

Program name: Message Encryptor / Decryptor

Description: This program can encrypt And decrypt messages based on a given table.
If run with the argument "encrypt", it asks the user for a message,
encrypts it, and saves it to encrypted_msg.txt.
If run with the argument "decrypt", it reads the file and decrypts the message.
The program assumes all characters appear in the table.

Date: 2025 - 10 - 13

"""
import logging
import sys

# Create and configure logger
logging.basicConfig(filename="newfile.log",format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
""""
# Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")
"""

encode_table = {
    'A':56,'B':57,'C':58,'D':59,'E':40,'F':41,'G':42,'H':43,'I':44,
    'J':45,'K':46,'L':47,'M':48,'N':49,'O':60,'P':61,'Q':62,'R':63,
    'S':64,'T':65,'U':66,'V':67,'W':68,'X':69,'Y':10,'Z':11,
    'a':12,'b':13,'c':14,'d':15,'e':16,'f':17,'g':18,'h':19,'i':30,
    'j':31,'k':32,'l':33,'m':34,'n':35,'o':36,'p':37,'q':38,'r':39,
    's':90,'t':91,'u':92,'v':93,'w':94,'x':95,'y':96,'z':97,
    ' ':98, ',':99, '.':100, "'":101, '!':102, '-':103
}

decode_table = {str(v): k for k, v in encode_table.items()}

def encrypted_msg():
    try:
        with open("encrypted_msg.txt", "r") as f:
            data = f.read().strip()
    except FileNotFoundError:
        logger.error("encrypted_msg.txt not found.")
        print("Error Please Check Logging File")
        return "File Not Found"
    if not data:
        logger.warning("Decrypted message is empty.")
        print("Warning Please Check Logging File")
        return ""
    return data

def encrypt(message):
    """
    Encrypts A Message Using The Encode Table
    Each One Of The Characters Is Being Replaced By Its Number Separated By Commas
    And Then Saves It In An Outer File
    """

    if not message:
        encrypted = ""
    else:
        nums = [str(encode_table[ch]) for ch in message if ch in encode_table]
        encrypted = ",".join(nums)
    return encrypted

def decrypt(encrypted_message):
    """
    Decrypts A Encrypted Str Back To Text
    Each One Of The Numbers Is A Character From The Decode Table
    """

    if encrypted_message == "":
        return ""

    nums = encrypted_message.split(",")
    chars = [decode_table[n] for n in nums]
    return "".join(chars)

def main():
    if len(sys.argv) < 2:
        logger.error("Get An Argument From The User")
        print("Error Please Check Logging File")
        sys.exit(1)

    action = sys.argv[1].lower()
    if action == "encrypt":
        logger.info("User Started Encrypting Function")
        message = input("What Is The Message You Want To Encrypt : ")
        encrypted = encrypt(message)
        with open("encrypted_msg.txt", "w") as f:
            f.write(encrypted)
        logger.info("Encrypted message saved to encrypted_msg.txt" + " The Message Is : " + encrypted + " From The Word : " + message)
        print("Encrypted message saved to encrypted_msg.txt")
    elif action == "decrypt":
        logger.info("User Started Decrypting Function")
        encrypted_message = encrypted_msg()
        if encrypted_message == "File Not Found":
            print("File Not Found Please Encrypt First")
        else:
            decrypted_msg = decrypt(encrypted_message)
            logger.info("User Just Decrypted Message saved to encrypted_msg.txt" + " The Message Is: " + decrypted_msg)
            print("The Decrypted Message Is : ")
            print(decrypted_msg)
    else:
        logger.error("User Didnt Enter Encrypt or Decrypt")
        print("Error Please Check Logging File")

if __name__ == "__main__":
    assert encrypt("hello world") == "19,16,33,33,36,98,94,36,39,33,15" , "Encrypt Test Falied"
    assert decrypt("19,16,33,33,36,98,94,36,39,33,15") == "hello world" , "Decryption Test Falied"
    logger.info("All Assert Test Passed")

main()




