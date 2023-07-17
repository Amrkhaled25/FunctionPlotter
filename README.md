# FunctionPlotter
This is a function plotter application built using PySide2. It allows you to visualize mathematical functions by plotting them on a graph.
## Installation

1. Clone the repository to your local machine:
git clone https://github.com/Amrkhaled25/FunctionPlotter.git

2. Install the required dependencies using pip:
pip install PySide2

3. Install pytest and pytest-qt for end-to-end testing:
pip install pytest pytest-qt

## Usage

1. Open a terminal and navigate to the project directory.

2. Run the following command to start the function plotter application:
python main.py

3. Enter your mathematical function in the provided input field. For example, you can enter `sin(x)`,`x^2`.

4. Click the "Plot" button to generate the graph.

## End-to-End Testing

End-to-end testing ensures that the function plotter works as expected. We use pytest and pytest-qt for automated testing.

To run the tests, follow these steps:

1. Open a terminal and navigate to the project directory.

2. Run the following command:
pytest
3. The tests will be executed, and you'll see the test results in the terminal.

## Working examples snapshots
![valid_input3](https://github.com/Amrkhaled25/FunctionPlotter/assets/116092948/e8607855-347b-4c6a-b9df-009aa4aea2a9)
![valid_input2](https://github.com/Amrkhaled25/FunctionPlotter/assets/116092948/fe8329ed-b543-49c4-82e5-fd826b0b29da)
![valid_input](https://github.com/Amrkhaled25/FunctionPlotter/assets/116092948/7f469a82-4afb-41b1-adcc-f49844d5e268)

## Wrong examples snapshots
![invalid_input](https://github.com/Amrkhaled25/FunctionPlotter/assets/116092948/72af7e37-c374-4a9f-8ae8-f473c26ad72d)
![invalid_input2](https://github.com/Amrkhaled25/FunctionPlotter/assets/116092948/d289b28e-3c8f-4efa-82d9-d4cfaf30a9dc)
![invalid_input3](https://github.com/Amrkhaled25/FunctionPlotter/assets/116092948/715bc27d-2f79-4ef0-8649-c15e75f27e5f)

