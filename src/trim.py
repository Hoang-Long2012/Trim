import sys
import argparse
def trim(Side=None, Chars=None):
	Methods = {
		None: str.strip,
		"l": str.lstrip,
		"r": str.rstrip
	}
	if Chars is not None:
		try:
			Chars = Chars.encode().decode("unicode_escape")
		except (ValueError, UnicodeError):
			print(f"Invalid escape sequence: {Chars!r}", file=sys.stderr)
			sys.exit(1)
	try:
		for Line in sys.stdin:
			Ending = ""
			if Line.endswith("\r\n"):
				Ending = "\r\n"
				Line = Line[:-2]
			elif Line.endswith("\n"):
				Ending = "\n"
				Line = Line[:-1]
			elif Line.endswith("\r"):
				Ending = "\r"
				Line = Line[:-1]
			Strip = Methods.get(Side)
			if Strip is None:
				raise ValueError(f"Invalid side: {Side}")
			Line = Strip(Line, Chars)
			print(Line, end=Ending)
	except KeyboardInterrupt:
		return None
def getVersion():
	return "1.0"
def parseArgs():
	Parser = argparse.ArgumentParser(prog="trim", description="Strip characters from the beginning and/or end of each input line.", allow_abbrev=False)
	Parser.add_argument("-v", "--version", action="version", version=f"Trim version {getVersion()}")
	Parser.add_argument("chars", nargs="?", type=str, metavar="CHARS", help="Custom characters to strip.")
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