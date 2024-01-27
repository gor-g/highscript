
import re
import pytest
from hscript import run
from hscript.terminal.terminal import RunInTerminalError


@pytest.mark.parametrize("cmd, fatal, debug, verbose, expected_return_code, expected_stdout, expected_stderr",  [ 
    (cmd, fatal, debug, verbose, expected_return_code, expected_stdout, expected_stderr)
    for cmd, expected_return_code, expected_stderr in [("echo 'Hello'", 0, ""),
                                                       ("echo 'Hello' && exit 1", 1, ""),
                                                       ("echo 'Hello' && echo 'This is an error' >&2 && exit 42", 42, "This is an error\n")]
    for fatal in [True, False]
    for debug in [True, False]
    for verbose in [True, False]
    for expected_stdout in ["Hello\n"]
])
def test_run(cmd, fatal, debug, verbose, expected_return_code, expected_stdout, expected_stderr, capsys):
    """
    Test the run function with different combinations of parameters.
    """
    pyexpected_stdout = ""
    pyexpected_stderr = ""
    if expected_return_code!=0:
        if verbose or debug:
            pyexpected_stdout +=f"Executed: {cmd}\n"
            pyexpected_stdout +=f"Command failed with return code: {expected_return_code}\n"
            pyexpected_stdout +=f"Standard Output: {expected_stdout}\n"
            pyexpected_stdout +=f"Standard Error: {expected_stderr}\n"
        if fatal:
            pyexpected_stderr +="Executed command returned an error code. Use debug=True to see more information. Use fatal=False to disable this error.(The runned command can still fail but this function wont raise an error.)"
    else:
        if verbose:
            pyexpected_stdout +=f"Executed: {cmd}\n"
            pyexpected_stdout +=f"Command executed successfully.\n"
            pyexpected_stdout +=f"Standard Output: {expected_stdout}\n"
    
    if fatal and expected_return_code != 0:
        with pytest.raises(RunInTerminalError, match=re.escape(pyexpected_stderr)):
            result = run(cmd, fatal=fatal, debug=debug, verbose=verbose)
    else:
        result = run(cmd, fatal=fatal, debug=debug, verbose=verbose)
        assert result.returncode == expected_return_code
        assert result.stdout == expected_stdout
        assert result.stderr == expected_stderr

    captured = capsys.readouterr()
    assert captured.out == pyexpected_stdout
