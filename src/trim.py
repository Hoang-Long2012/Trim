import sys
import ast
import argparse
def decode_escape(Value):
	if Value is None:
		return None
	try:
		Result = ast.literal_eval('"' + Value.replace('"', '\\"') + '"')
		if not isinstance(Result, str):
			raise ValueError
		return Result
	except (SyntaxError, ValueError, UnicodeError):
		print(f"Invalid escape sequence: {Value!r}", file=sys.stderr)
		sys.exit(1)
def trim(Side=None, Whitespace=False, Chars=None, End=None):
	Methods = {	
		None: str.strip,
		"l": str.lstrip,
		"r": str.rstrip
	}
	Chars = decode_escape(Chars)
	End = decode_escape(End)
	Strip = Methods.get(Side)
	if Strip is None:
		raise ValueError(f"Invalid side: {Side}")
	for Line in sys.stdin:
		Ending = ""
		if End is None:
			if Line.endswith("\r\n"):
				Ending = "\r\n"
				Line = Line[:-2]
			elif Line.endswith("\n"):
				Ending = "\n"
				Line = Line[:-1]
			elif Line.endswith("\r"):
				Ending = "\r"
				Line = Line[:-1]
		else:
			Ending = End
		if Whitespace:
			Line = Strip(Line)
		Line = Strip(Line, Chars)
		sys.stdout.write(Line + Ending)
def parseArgs():
	Parser = argparse.ArgumentParser(prog="Trim", description="Strip characters from the beginning and/or end of each input line.", allow_abbrev=False)
	Parser.add_argument("-v", "--version", action="version", version="%(prog)s version 1.3")
	Parser.add_argument("chars", nargs="?", type=str, metavar="CHARS", help="Custom characters to strip.")
	Parser.add_argument("-w", "--whitespace", action="store_true", help="Strip junk characters even when a custom character set has been specified.")
	Parser.add_argument("-e", "--end", type=str, metavar="ENDING", help="Line ending of output.")
	Side = Parser.add_mutually_exclusive_group()
	Side.add_argument("-r", "--right", action="store_true", help="Strip only the end of the line.")
	Side.add_argument("-l", "--left", action="store_true", help="Strip only the start of the line.")
	Args = Parser.parse_args()
	if Args.whitespace and not Args.chars:
		Parser.error("-w; --whitespace require chars")
	return Args
def main():
	Args = parseArgs()
	Side = None
	if Args.right:
		Side = "r"
	elif Args.left:
		Side = "l"
	try:
		trim(Side, Args.whitespace, Args.chars, Args.end)
	except KeyboardInterrupt:
		sys.exit(130)
if __name__ == "__main__":
	main()