import argparse
import sys
import subprocess
import time
import pyfiglet

ALGORITHMS = {
    8: {64: 'BASE64, CRC32'},
    24: {192: 'MD5(base64)'},
    32: {256: 'MD5, NTLM, MD4'},
    40: {320: 'SHA-1, MYSQL5'},
    60: {480: 'BCRYPT'},
    16: {128: 'MYSQL'},
    35: {280: 'md5(md5($pass).$salt); VB; DZ'},
    54: {432: 'MSSQL2015'},
    64: {512: 'SHA-256'},
    128: {1024: 'SHA-512, WHIRLPOOL'},
    96: {768: 'SHA-384'},
}

def load(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.30)

def clear_screen():
    subprocess.Popen("cls" if sys.platform == "win32" else "clear")

def pesan(inpt, detect_char, byte_size, algo):
    print(f"[+] Hash: {inpt}\n[+] Algorithms: {algo}\n[+] Length: {detect_char}\n[+] Bit: {byte_size}\n\n[!] Successfully Analyzed.....")

def checking_hash(inpt):
    detect_char = len(inpt)
    byte_size = detect_char * 8

    print("Analyzed", end="")
    load("......")
    time.sleep(0.20)

    algo = ALGORITHMS.get(detect_char, {}).get(byte_size, 'Not Detected')
    pesan(inpt, detect_char, byte_size, algo)

def main():
    print(pyfiglet.figlet_format("Hash Identifier"), end="Mengidentifikasi jenis hash yang digunakan pada teks atau data yang terenkripsi\n\n[@] Author: Fierza-Dev\n[-] Version : 1.0.3 ( Realese )\n\n")
    
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-cp', '--cipher', help='CipherText', dest='cp', required=True)
        arg = parser.parse_args()
        inpt = arg.cp
        checking_hash(inpt)
    except KeyboardInterrupt:
        print("\n[!] User Interrupted.")
        sys.exit()

if __name__ == '__main__':
    if sys.version_info < (3, 0):
        sys.stdout.write("[!] Sorry, Hash-Identifier requires Python 3.x\n")
        sys.exit(1)
    else:
        clear_screen()
        main()

