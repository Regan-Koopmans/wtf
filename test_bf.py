import io
import sys
from bf import run

def test_bf():
    # Capture stdout of function 
    capturedOutput = io.StringIO() # Create StringIO object
    sys.stdout = capturedOutput #  and redirect stdout.
    # Call function.
    run("""
        ++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.
        +++++++..+++.>++.<<+++++++++++++++.>.+++.------.
        --------.>+.>.
        """)
    assert capturedOutput.getvalue() == 'Hello World!\n'