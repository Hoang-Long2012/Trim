# Trim

trim is a small tool to strip characters from the beginning and/or end of each input line.

## Features

- Strip characters from both sides of a line.
- Strip characters only from the beginning (`--left`).
- Strip characters only from the end (`--right`).
- Supports custom characters.
- Supports escaped characters such as `\n`, `\t`, etc.
- Works with standard input and output, making it suitable for pipelines.

## Installation

### From release

Download latest version from [Release page](https://github.com/Hoang-Long2012/trim/releases/latest) and extract.

### From source

- Clone this repository:

```
git clone https://github.com/Hoang-Long2012/trim.git
```

- Run:

```
cd src
python trim.py
```

### Build executable

- Install PyInstaller:

```
pip install pyinstaller
```

- Build:

```
pyinstaller --onefile --name trim trim.py
```

## Usage

```
trim [OPTIONS] [CHARS...]
```

`trim` reads text from standard input, processes each line, and writes the result to standard output.

## Examples

- Remove spaces from both ends:

```
echo "   Hello World   " | trim
```

Output:

```
Hello World
```

- Remove custom characters:

```
echo "xxxHello Worldxxx" | trim x
```

Output:

```
Hello World
```

- Remove only the right side:

```
echo "Hello Worldxxx" | trim -r x
```

Output:

```
Hello World
```

- Remove only the left side:

```
echo "xxxHello World" | trim -l x
```

Output:

```
Hello World
```

## Options

| Option | Description |
| --- | --- |
| `-v`, `--version` | Show program version. |
| `-h`, `--help` | Show help message. |
| `-r`, `--right` | Strip characters only from the end of the line. |
| `-l`, `--left` | Strip characters only from the beginning of the line. |
| `-w`, `--whitespace` | Strip junk characters even when a custom character set has been specified. |
| `CHARS` | Characters to strip. |

## Custom Characters

The `CHARS` argument specifies the characters that should be removed.

## Note

`CHARS` is treated as a character set, not a string. For example:

```
trim abc
```

removes any combination of `a`, `b`, and `c` characters from the beginning and end of each line.

## Escape Sequences

`trim` supports escape sequences in the character argument.

### Examples:

```
trim "\\t"
```

Remove tab characters.

```
trim "\\n"
```

Remove newline characters.

	## License

	This project is licensed under the [MIT License.](LICENSE)

TCopyright (c) 2026 Hoàng Long
