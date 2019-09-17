# SOČ Template
This repository contains the source code of [SOČ](http://www.soc.cz/) paper template written in LaTeX. It can be used for any educational purpuse.

## Compiling the paper
If you want to use the project as a template for your own SOČ paper, or to compile the paper, there are some things you should know before doing so.


### Typesetting system
The paper was converted to PDF using **LuaTeX**. It was chosen mainly for its out-of-the-box UFT-8 support (which pdfTeX lacks). It comes with most of the major TeX distributions like TeX Live and MiKTeX, so you should already have it installed. If you need any help with setup, you can contact me on [j.cerny.zdar@gmail.com](email:j.cerny.zdar@gmail.com)

[compile.py](scripts/compile.py) is the script that is used to build the paper. I would recommend you either use it directly or run the same commands in the command line to properly render things like bibliography or the list of acronyms.

```
python3 compile.py
```

### Code Highlights
_If you don't need code highlights, simply remove `\usepackage{minted}` from `paper.tex` and skip the rest of this section._

Code highlights in the paper use the minted package, which uses **Pygments** (a Python syntax highlighter). To install it, run this command in your terminal:

```
pip install Pygments
```

You can then run `pygmentize -V` to ensure that the program installed correctly. Keep in mind that you will need to run the compilation with the `--shell-escape` option to allow shell interaction (see [compile.py](scripts/compile.py)).


### Fonts
The font **CMU Serif** was used to typeset the (majority of the) paper, mainly due to it's bold small caps support that SOČ requires for certain headings. Make sure to have it [installed](https://sourceforge.net/projects/cm-unicode/) either on your system or through your TeX distribution if you plan on using it.

You can also use a different system font by changing the line `\setmainfont{CMU Serif}` in `paper.tex`.

The paper also uses **FontAwesome5** and the fontawesome5 package to typeset certain symbols and icons. You can either remove the line `\usepackage{fontawesome5}` from `paper.tex` if you don't plan on using any of the icons, or [install the font](https://fontawesome.com/download) on your system.

## About
This tamplate would not be possible to make without [Tomáš Sláma](slama.dev) and his awesome work and support. Every time you download this template, you should stand up and salute his honor.
