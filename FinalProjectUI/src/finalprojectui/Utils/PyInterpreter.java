/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package finalprojectui.Utils;

import org.python.core.*;
import org.python.util.PythonInterpreter;

/**
 *
 * @author dell
 */

//A singleton class that provides Jython Python interpreter.
public class PyInterpreter {
    private static PyInterpreter _instance;
    private PythonInterpreter _interpreter;
    public final String SRC_PATH="C:\\Users\\dell\\Documents\\GitHub\\MinerAnalyzer\\MinerAnalyzer";
    
    public static PyInterpreter getInstance()
    {
        if(_instance==null)
        {
            _instance=new PyInterpreter();
        }
        return _instance;
    }
    
    private PyInterpreter()
    {
        _interpreter = new PythonInterpreter(null, new PySystemState());
        PySystemState sys = Py.getSystemState();
        sys.path.append(new PyString(SRC_PATH));
        
    }

    public PyObject exec(String filePath, String evalCommand)
    {
        _interpreter.execfile(SRC_PATH+"\\"+filePath);
        return _interpreter.eval(evalCommand);
    }
    
    public void execFile(String filePath)
    {
        _interpreter.execfile(SRC_PATH+"\\"+filePath);
    }
    
    public PyObject eval(String evalCommand)
    {
        return _interpreter.eval(evalCommand);
    }
}
