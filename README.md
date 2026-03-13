# goph547-w2026-Midterm1-ZS
Semester: W2026  
Instructor: B. Karchewski  
Author(s): Zac Strei  

Semester: W2026  
Instructor: B. Karchewski  
Author(s): Zac Strei  

This repository contains the code and outputs for **Midterm #1 of GOPH 547 (Winter 2026)**. The midterm covers topics related to gravitational potential fields, vector calculus operations, gravitational flux, equivalent surface density, and theoretical gravity in a rotating reference frame. The problems require both analytical derivations and numerical calculations using Python. The provided scripts implement the calculations used to solve the quantitative portions of the midterm and generate the outputs and visualizations used to interpret the results. The exam consists of conceptual multiple-choice questions as well as analytical and computational problems involving gravitational fields, divergence, flux integrals, spherical coordinate systems, and gravity effects from subsurface mass anomalies. 

The recommended way to download or clone the repository is by navigating to the desired directory in a terminal using the command:

```
cd /path/to/directory
```

Then run either:

```
git clone https://github.com/Zstrei/goph547-w2026-Midterm1-ZS.git
```

or

```
gh repo clone Zstrei/goph547-w2026-Midterm1-ZS
```

if the GitHub CLI is installed. This will download the repository files into a new local directory. The repository can also be downloaded by clicking the green CODE button on GitHub and selecting “Download ZIP.” Be sure to navigate to the directory where the files will be stored before cloning.

It is recommended to set up a virtual environment when running the files. To create a virtual environment, navigate to the repository directory and run:

```
python -m venv .venv
```

To activate it in PowerShell, run:

```
.\.venv\Scripts\activate
```

On macOS/Linux, run:

```
source .venv/bin/activate
```

After activation, “(.venv)” should appear in the terminal.

Install the required packages using:

```
pip install numpy matplotlib setuptools
```

### Example Files

The `examples` directory contains the files corresponding to the computational portions of the midterm.

`part-1.txt` contains the written answers for the conceptual and theoretical questions from Part I of the midterm. These responses address topics such as gravitational field properties, Newton’s law of gravitation, gravity gradients, rotating reference frames, and the geoid.

`part-2.py` implements the calculations required for the vector operations and curvilinear coordinate analysis. The script computes gravitational field components, evaluates vector operations such as divergence, and performs numerical calculations using the Cartesian form of the gravitational potential.

`part-3.py` performs the calculations related to gravitational flux and equivalent surface density for subsurface mass anomalies. The script evaluates the flux integral through the integration surface and computes the equivalent surface density for the mass distribution.

`part-4.py` implements the calculations for theoretical gravity on a rotating Earth. This includes evaluating the gravitational and centrifugal contributions to gravity and comparing the theoretical estimate with values obtained using an International Gravity Formula.

NOTE: All derivations required to answer the questions are found in the comments of the code for each specific part of each question. All questions requiring comments/comparisons on data can be found in the "Final outputs" section of the code, usually found near the bottom of the program as well as printed in the output of the code 
