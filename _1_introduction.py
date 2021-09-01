

'''
Guido Van Rosuum is Invented Python.[Late 1980's and early 1990's]
Python is The Combination of most powerfull scripting launguage and most powerful programming launguage
Python  = most powerfull scripting launguage + most powerful programming launguage

Powerful scripting launguage:-
----------------------------
1) PERL (Practical Extraction and Reporting Launguage.)
    a) Efficient for string's patterns matching, by using Regular expression's
    b) It can use more number of symbol's to evaluate the powerful regular expression's
    c) It's very tough to remember or operate all those symbol's for programmer or developer.
Python can do all these works very easily.

JAVA:-
----
1) Java is the powerfull programming launguage
2) Java simplified the programming burdens of C,C++
3) But Python made programming more easier than Java

        Java comes from C/C++ - launguage's .Here in c-launguage the programming complexity is
one of the disadvantage. It is a procedure oriented launguage because of that reason here
procedures are having lot of priority.Here programming length should be very high.

                For that adding one concept called class for C-launguage and it becomes class
with C and now a days we call it as C++.
                Here in C++ they consider some disadvantage's and they simplify all the
disadvantages by creating Java.This java is also simplified by Python.

                For accessing a system calls TCL is the best launguage .some times this TCL is
also depending on the TK for GUI  application's.And Python made this more easier.


Advantage's of Python :-
---------------------
1) High level launguage.
2) Object oriented launguage.
3) Easy to Read.
4) Easy to Understand.
5) Easy to Learn.
6) Python is Interpreted.
7) Python is Interactive.
8) Python is Beginer's launguage.
9) Python can develop small small Application's.
10) Python can develop large Application's.

Application's of Python :-
------------------------
1) Artificial Inteligence
2) Automation and Web application's
3) Gui Application's
4) Scientific and Business Application's
5) Console Based Appliction's
6) Audio and Video Based Applicaion's
7) Enterprise Application's


What is a Compiler:-
-------------------
1)           A compiler is a program that translates a source language or high-level
programming language (for example, Java, C++) into a target machine code (binary bits – 1 and 0)
that the CPU can process and understand.
2)         The program to be translated is written inside an editor and are known as source
statements.The act of translating source code to machine or binary code is known as compilation.
3)          A compiler that is suitable for the programming language is used in which the name
of the file name containing the source statements is specified.
4)          During compilation, all the language statements will be parsed or analyzed to
see if it is correct. If there is no error, the compiler would then convert the source code
into machine code which is then ready to execute.
5)             The output of the compilation is also known as object code or object module.
6)             However, it should not be confused with an object in object-oriented programming
as it is not the same.
7)             The task of a compiler is generally divided into several phases. The phases
include lexical analysis, syntax analysis, sematic analysis,intermediate code generator,
code optimizer and code generator. Each of these phases helps convert the source code by
breaking it down into tokens, generating parse trees and optimizing the source code.


What is an Interpreter:-
----------------------

1)             An interpreter is a program which also converts a high-level programming
language (like Python, PHP, Perl) into machine code.
2)            Although similar to a compiler, the way that code is executed is different for
both. Unlike a compiler that simply converts the source code to machine code,
3)             An interpreter can be run directly as an executable program. Contrary to a compiler,
it converts source code to machine code when the program is running and not before the
program runs.
4)          Interpreters do not produce any intermediary object code like compilers.
5)          In interpreters, the source code is compiled and executed at the same time.
It continues to translate the program until it encounters the first error after which it stops.
Therefore, it is easy to debug.
6)          With interpreters, the source statements are executed line by line in contrast to a
compiler that converts the whole program at once.
7)          The interpreter also performs lexing, parsing and type checking which is similar
to a compiler.
 9)        However, interpreters directly process syntax tree rather than generating code
from it.


Python Interpreter:-

1)  Python is generally referred to as an interpreted language.
2)  This means that each line of code is executed one by one.
3)  However, it does involve the process of compilation.
4)  The reason why Python is termed as an interpreted language is that the compiler in Python
does relatively less work than an interpreter or in a compiled language like C or Rust.
5)  However, a programming language in itself has no said as to where it is compiled or
interpreted. Rather, it is the property of the implementation that decides this.
6) The Python interpreter is generally installed as /usr/local/bin/python if it happens
to be available in the system.
7) In Python, compilation takes place where the code compiles into a simpler form called
bytecode.
8) The byte code is not really interpreted to machine code unless there is some kind of
implementation like PyPy.
9) Bytecodes are executed by Python Virtual Machine (PVM) which emulates a simplified
execution environment.
10) The compilation process to bytecode is entirely implicit.
11) This means that you never invoke the compiler. Instead, you simply run a .py file.
12) The lack of an explicit compile step is why the Python executable is known as the Python
interpreter.
13) The first step of an interpreter is to read a Python code or instruction.
It then checks the syntax of each line and verifies if the instruction is well-formatted.
The interpreter can display the errors of each line one by one.
An important feature of Python is it’s interactive prompt.
A Python statement can be typed and immediately executed.
Most of the compiled languages may not have this interactivity.
Python is compiled to bytecode and this bytecode is immediately executed without an
explicit compile step.


Different Python implementations :-                  [GangBoard]
----------------------------------
[Compiler & Interpreter in Python | Different ... - GangBoardwww.gangboard.com › Blog › python]

PyPy:-
----
1)              PyPy is a Python interpreter that is developed based on RPython –
a subset of Python programming language.
2)         A lot of programmers prefer PyPy over other implementations as it offers optimal
speed and performance. The interpreter can understand and interpret
3)     the Python source code very quickly and efficiently. It comes with a built-in Just-in-Time or JIT compiler.
4)     The JIT compiler is used to make PyPy interpret source codes much speeder than other
interpreters.
5)  PyPy can also be used by developers to efficiently execute long-running codes.
Various studies show that Python is more memory hungry as compared to other programming
languages. As such, developers try to find ways to reduce the consumption of memory
without affecting the performance of the Python application.
Since PyPy is way lighter than the interpreters that are written in C programming
language like CPython, it reduces memory consumption.


 CPython:-
 -------
1)     CPython is the original implementation for Python and has been written in C programming
language.
2)      CPython is an interpreter that provides a foreign function interface with C as well as
other programming languages.
3)      It compiles a Python code into intermediate bytecode which is interpreted by the
CPython virtual machine. It also acts as a compiler as it transforms Python code to bytecode
before it is interpreted.
4)      CPython is best if you are writing an open-source code Python code and wish to reach a
larger audience. CPython also offers the advantage of speeding up code.
5)     CPython also offers the highest level of compatibility with Python packages as well as
C extension modules.


Jython:-
------

1)     Jython is another implementation of Python which compiles a Python code to Java
bytecode.
2)    Using Jython, we can run Python on any environment that supports and runs a  Java Virtual
Machine or JVM. Moreover, it has the ability to import and use any Java class like a Python
module. Jython supports both static and dynamic compilation.

IronPython:-
-----------

1)     IronPython is an open-source implementation of Python and is firmly integrated with
the .NET framework.
2)    IronPython can use both .NET frameworks as well as Python libraries.
3)    It supports dynamic compilation has come with an interactive console.


Byterun : -
-------

1)     Byterun is a compact Python interpreter written in Python. It was originally
created as a learning exercise and is easy to understand partly
2)    Because it is written in a high-level language that many people can easily read and
understand. One of the disadvantages of Byterun is its speed.


'''