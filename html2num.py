#!/usr/bin/python3

import subprocess, sys, argparse, os

parser = argparse.ArgumentParser(usage=f" python3 {sys.argv[0]} --string \"<h1>Simple Example</h1>\""
		f"\n\tpython3 {sys.argv[0]} --file=/home/user/file --output=file.xyz")

group_ex = parser.add_mutually_exclusive_group()
group_ex.add_argument("-s", "--string", help="Enter the html command you want to convert (no escape characters)", metavar='"<h1>example</h1>"')
group_ex.add_argument("-f", "--file", help="Enter the html file you want to convert", metavar="/path/to/file")
parser.add_argument("-o", "--output", help="The name of the file in which the output will be saved", metavar="file.xyz", default=False)
parser.add_argument("-x", "--xclip", help="Copy the content of the generated file", action="store_true", default=False)
args = parser.parse_args()

ascii = []

if __name__ == '__main__':

	string = args.string
	file = args.file
	output = args.output
	xclip = args.xclip

	if string:
		for line in string:
			ascii.append(f"&#{ord(line)};")

		print("[*] Converted.\n")
		for line, char in zip(ascii, string):
			print(line + " = " + char)

		subprocess.Popen(f"echo {ascii} | sed 's/, //g' | sed 's/\[//g' | sed 's/\]//g' | xclip -sel clip", shell=True)
		print("\n\n[*] Copied to clipboard.")

	if file:
		if output:
			if os.path.isfile(file):
				print("[*] File detected, File Name: ", end=" ")
				with open(file, "r") as f:
					print(f.name)
					lines = []

					for line in f.readlines():
						if "\t" in line:
							line = line.replace("\t", "    ")
						lines.append(line)

					for line in lines:
						for char in line:
							ascii.append(f"&#{ord(char)};")

				with open(output, "w") as f:
					for ascii_char in ascii:
						f.write(ascii_char)

				print("[*] Successfully generated file.")
				print(f"[*] The path of the file: {os.getcwd()}/{output}")

				if xclip:
					print(f"[*] Copying file content: '{output}'.")
					subprocess.Popen(f"xclip -sel clip {output}", shell=True)
					print(f"[*] Successfully copied")

			elif os.path.isdir(file):
				print("[!] Directory detected, exiting...\n")
				sys.exit(1)

			else:
				print("[!] Verify the path, exiting...")
				sys.exit(1)

		else:
			print("[*] The output parameter is necessary, exiting...\n")
			sys.exit(1)