#!/usr/bin/python3

import subprocess, sys, argparse, os

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("--oneline", help="Enter the html command you want to convert", metavar='"<h1>example</h1>"')
group.add_argument("--file", help="Enter the html file you want to convert", metavar="/path/to/file")
args = parser.parse_args()

ascii = []

if __name__ == '__main__':

	if args.oneline:
		for line in args.oneline:
			if "\t" in line:
				line = line.replace("\t", " ")

			for char in line:
				ascii.append(f"&#{ord(char)};")

		print()
		for num in ascii:
			print(num, end="")

		print("\n\n\t[*] Copied to clipboard\n")
		subprocess.run(f"echo {ascii} | sed 's/\[/ /g' | sed 's/\]/ /g' | tr -d ' ,\n' | xclip -sel clip", shell=True)

	if args.file:
		if os.path.isfile(args.file):
			with open(args.file, "r") as f:
				for lines in f.readlines():
					if "\t" in lines:
						lines = lines.replace("\t", " ")

					for char in lines:
						ascii.append(f"&#{ord(char)};")
			print()
			for num in ascii:
				print(num, end="")

			print("\n\n\t[*] Copied to clipboard\n")
			subprocess.run(f"echo {ascii} | sed 's/\[/ /g' | sed 's/\]/ /g' | tr -d ' ,\n' | xclip -sel clip", shell=True)
		else:
			if os.path.isdir(args.file):
				print("[!] Directory detected.")
				sys.exit(1)

			else:
				print("[!] Check if the path you entered exists")
				sys.exit(1)