import os
import subprocess

# easier to change for running the Tex commands
file_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_dir + os.sep + "..")

# this makes it so that the name of the Tex file isn't hardcoded
file_name = [f for f in os.listdir(".") if f.endswith(".tex")][0][:-len(".tex")]

# clean-up files from the previous compilation to perform a clean one
for file in [f for f in os.listdir(".") if os.path.isfile(f)]:
    if file.startswith(file_name) and not file.endswith(("tex", "bib", "xoj")):
            os.remove(file)

# initial lualatex run
os.system("lualatex --shell-escape %s.tex" % file_name)

# build bibliography
os.system("biber %s" % file_name)

# build glossaries
os.system("makeglossaries %s" % file_name)

# run lualatex enough times to correctly typeset cross-reference-related text
for _i in range(3):
    os.system("lualatex --shell-escape %s.tex" % file_name)
