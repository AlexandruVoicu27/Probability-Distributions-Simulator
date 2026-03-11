**Project Overview**

  This project is an interactive Python-based desktop application designed to simulate various probability distributions and random vectors. The software logs the generated empirical data and provides intuitive graphical representations to compare theoretical models with simulated outcomes.
The application follows a modular architecture, cleanly separating the graphical user interface, the mathematical simulation logic, and the data visualization components.

**Core Features**

The simulations are categorized into three main areas, accessible through a user-friendly main menu:

Discrete Random Variables: Allows users to simulate Bernoulli, Binomial, Geometric, Poisson, and Discrete Uniform distributions.

Continuous Random Variables: Provides simulations for Exponential, Continuous Uniform, and Normal distributions. It utilizes standard mathematical generation algorithms, such as the Box-Muller transform for the Normal distribution.

Uniformly Distributed Random Vectors (2D): Generates and plots 2D coordinates representing points uniformly distributed across specific geometric domains: a Rectangle, a Disk (Circle), and an Ellipse.

**Technical Architecture**

The codebase is structured around three primary Python scripts:

meniu.py (Graphical User Interface): Built using the tkinter and ttk libraries, this module provides the frontend. It guides the user through selecting a distribution and inputting specific mathematical parameters (e.g., probability $p$, mean $\mu$, standard deviation $\sigma$, or the total number of simulations).

simulari.py (Simulation Logic): Acts as the backend engine. It leverages Python's built-in random and math modules to generate the randomized data based on the user's input. For data persistence and traceability, the raw outcomes are temporarily exported to text files within a dedicated Simulari\ directory.

grafice.py (Data Visualization): Responsible for the visual output. It reads the raw data from the generated text files and uses the numpy and matplotlib.pyplot libraries to render appropriate charts—such as bar charts, histograms, or scatter plots.

**How to Run**
Ensure you have Python installed on your system, along with the numpy and matplotlib libraries.

Launch the application by running the start.bat file. Alternatively, you can run the following command in your terminal: python meniu.py.

Navigate the main menu to select the desired random variable or vector.

Input the required theoretical parameters and click "Simulează" (Simulate) to process the data and view the resulting plot.
