import sys
import os
import argparse
def trim(Side=None, Chars=None):
	if Chars is not None:
		try:
			Chars = Chars.encode().decode("unicode_escape")
		except (ValueError, UnicodeError):
			print(f"Invalid escape characters: {Chars}", file=sys.stderr)
	try:
		for Line in sys.stdin:
			NewLine = Line.endswith("\n")
			Line = Line.removesuffix("\n")
			if Side is None:
				Line = Line.strip(Chars)
			elif Side == "r":
				Line = Line.rstrip(Chars)
			elif Side == "l":
				Line = Line.lstrip(Chars)
			print(Line, end="\n" if NewLine else "")
	except KeyboardInterrupt:
		return None
def getVersion():
	return "1.0"
def parseArgs():
	Parser = argparse.ArgumentParser(prog="Trim", description="A small tool to strip garbage characters at the beginning and end of your input line.", allow_abbrev=False)
	Parser.add_argument("-v", "--version", action="version", version=f"Trim version {getVersion()}")
	Parser.add_argument("chars", nargs="?", type=str, metavar="[CHARS...]", help="Custom character you want to strip.")
	Side = Parser.add_mutually_exclusive_group()
	Side.add_argument("-r", "--right", action="store_true", help="Strip only the end of the line.")
	Side.add_argument("-l", "--left", action="store_true", help="Strip only the start of the line.")
	return Parser.parse_args()
def main():
	Args = parseArgs()
	Side = None
	if Args.right:
		Side = "r"
	elif Args.left:
		Side = "l"
	trim(Side, Args.chars)
	sys.exit(0)
if __name__ == "__main__":
	main()