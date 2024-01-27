import subprocess

class RunInTerminalError(Exception):
    pass

def run( cmd, fatal = True, debug= True, verbose = False):
    """
    A wrapper for subprocess.run() that allows to print the command 
    before executing it and to print the output after the execution.
    It also allows to raise an error if the command fails.

    Parameters
    ----------
    cmd : str command to execute
    debug : bool shows error informaition when error occured
    verbose : bool show informaition wether the error occured or not
    fata: bool raises an error, hence stops either program flow or subprocess, if the command fails
    
    Returns 
    -------
    subprocess.CompletedProcess object.
    """
    
    result  = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    
    if result.returncode!=0:
        if verbose or debug:
            print(f"Executed: {cmd}" )
            print(f"Command failed with return code: {result.returncode}" )
            print(f"Standard Output: {result.stdout}")
            print(f"Standard Error: {result.stderr}")
        if fatal:
            raise RunInTerminalError("Executed command returned an error code. Use debug=True to see more information. Use fatal=False to disable this error.(The runned command can still fail but this function wont raise an error.)")
    else:
        if verbose:
            print(f"Executed: {cmd}" )
            print("Command executed successfully.")
            print(f"Standard Output: {result.stdout}")
        
    return result
