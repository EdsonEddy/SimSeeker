# SimSeeker

A Python code analysis tool using ANTLR for parsing and analyzing Python source code.

## Overview

SimSeeker leverages ANTLR (ANother Tool for Language Recognition) to parse Python code and generate analysis tools. This project includes grammar files for Python 3 and generates lexers, parsers, and visitors for code analysis.

## Prerequisites

- Python 3.x
- Java (for ANTLR)
- curl (for downloading dependencies)

## Setup

### 1. Install Python Dependencies

```sh
pip install antlr4-python3-runtime
```

### 2. Download ANTLR and Grammar Files

Run the following commands from the project root:

```sh
# Create tools directory and download ANTLR
mkdir -p tools
curl -o tools/antlr-4.13.1-complete.jar https://www.antlr.org/download/antlr-4.13.1-complete.jar

# Download Python grammar files
cd grammar
curl -O https://raw.githubusercontent.com/antlr/grammars-v4/master/python/python3/Python3Lexer.g4
curl -O https://raw.githubusercontent.com/antlr/grammars-v4/master/python/python3/Python3Parser.g4
cd ..
```

### 3. Generate Parser Files

```sh
cd grammar
java -jar ../tools/antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor -o ../gen Python3Parser.g4 Python3Lexer.g4
cd ..
```

### 4. Download Python3LexerBase and Python3ParserBase Files
```sh
cd gen
curl -O https://raw.githubusercontent.com/antlr/grammars-v4/master/python/python3/Python3/Python3LexerBase.py
curl -O https://raw.githubusercontent.com/antlr/grammars-v4/master/python/python3/Python3/Python3ParserBase.py
cd ..
```

### 5. Fix generated files
The generated files may need some adjustments to work correctly. Open the files in `gen/` and make the following changes:
- In `Python3Lexer.py`, replace `this.` with `self.`.
```sh
sed -i '' 's/this\./self\./g' gen/Python3Lexer.py
```

## Project Structure

```
├── grammar/          # ANTLR grammar files
├── gen/             # Generated parser files
├── src/             # Source code
├── tools/           # ANTLR jar file
└── README.md
```

## Usage

After setup, the generated parser files in the `gen/` directory can be used to parse and analyze Python code. The visitor pattern is enabled for traversing the abstract syntax tree.

## License

See [LICENSE](LICENSE) file for details.