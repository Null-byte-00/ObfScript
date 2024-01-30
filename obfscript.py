import argparse
from powershell import PowershellAddComment, PowershellValObf, PowershellVarObf, process_ps

def header():
    print("----- ObfScript v0.1.0 -----")
    print("By: Soroush(Amirali) Rfie")
    print("Github: Null-byte-00")
    print("----------------------------")


if __name__ == '__main__':
    header()
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input file", metavar="", required=True)
    parser.add_argument("-n", "--negetropy", help="the more the negetropy less complexitys", metavar="")
    parser.add_argument("-s", "--size", help="size of output script", metavar="")
    parser.add_argument("-c", "--add-comment", help="add random comments to output", action="store_true")
    parser.add_argument("-o", "--out", help="name of output file", metavar="")
    parser.add_argument("-l", "--language", help="script language: vb(VBScript) js(JScript) ps(Powershell script)", metavar="")
    parser.add_argument("-v", "--change-value", help="Obfuscate true/false/null .... values", action="store_true")
    args = parser.parse_args()
    process_ps(args)