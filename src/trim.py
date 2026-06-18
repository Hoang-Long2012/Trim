import sys
import argparse
def trim(Side=None, Chars=None):
	for Line in sys.stdin:
		if Side is None:
			print(Line.strip(str(Chars)), end="")
		elif Side == "r":
			print(Line.rstrip(str(Chars)), end="")
		elif Side == "l":
			print(Line.lstrip(str(Chars)), end="")
	return 0
def getVersion():
	return "1.0"
def parseArgs():
	Parser = argparse.ArgumentParser(prog="Trim", description="A small tool to strip garbage characters at the beginning and end of your input line.", 
if __name__ == "__main__":
	sys.exit(trim())