## First step

1. Change to the grammar directory.
    ```sh
    cd grammar
    ```
2. Generate utility files.
    ```sh
    java -Xmx500M -cp "../tools/antlr-4.13.1-complete.jar" org.antlr.v4.Tool \
    -Dlanguage=Python3 \
    -visitor \
    -o ../gen Python3Parser.g4 Python3Lexer.g4
    ```