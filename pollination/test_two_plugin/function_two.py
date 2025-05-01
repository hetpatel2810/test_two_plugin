from dataclasses import dataclass;
from pollination_dsl.function import Function, command, Inputs, Outputs;


@dataclass
class MyFunctionTwo(Function):
    """ My Function Two """

    # inputs
    input_file_path = Inputs.file(
        description="Path to input text file.",
        path="function_two_folder\input.txt"
    );

    @command
    def create_output_file(self):
        return '@((Get-Content function_two_folder\input.txt),"Message from Function 2")|Set-Content function_two_folder\output.txt';

    
    # outputs
    output_file_path = Outputs.file(
        description="Path to output text file.", 
        path="function_two_folder\output.txt"
    );
