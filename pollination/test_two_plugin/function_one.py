from dataclasses import dataclass;
from pollination_dsl.function import Function, command, Inputs, Outputs;


@dataclass
class MyFunctionOne(Function):
    """ My Function One """

    # inputs
    input_file_path = Inputs.file(
        description="Path to input text file.",
        path="function_one_folder\input.txt"
    );

    @command
    def create_output_file(self):
        return '@((Get-Content function_one_folder\input.txt),"Message from Function 1")|Set-Content function_one_folder\output.txt';

    
    # outputs
    output_file_path = Outputs.file(
        description="Path to output text file.", 
        path="function_one_folder\output.txt"
    );