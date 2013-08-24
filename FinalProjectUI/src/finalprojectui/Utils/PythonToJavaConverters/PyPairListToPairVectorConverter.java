/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package finalprojectui.Utils.PythonToJavaConverters;

import finalprojectui.Entities.Pair;
import java.util.Vector;
import org.python.core.*;

/**
 *
 * @author dell
 */
public class PyPairListToPairVectorConverter {
    public static Vector<Pair<Integer,Double>> convert(PyList list)
    {
        Vector<Pair<Integer,Double>> res=new Vector<Pair<Integer,Double>>();
        PyObject[] arr=list.getArray();
        for(int i=0; i<arr.length; i++)
        {
            PyInteger key=(PyInteger)arr[i].__getattr__("key");
            PyObject res1=arr[i].__getattr__("value");
            if(res1 instanceof PyLong)
            {
                PyLong value=(PyLong)arr[i].__getattr__("value");
                res.add(new Pair<Integer,Double>(key.asInt(),value.asDouble()));
            }
            else
            {
                PyFloat value=(PyFloat)arr[i].__getattr__("value");
                res.add(new Pair<Integer,Double>(key.asInt(),value.asDouble()));
            }
        }
        return res;
    }
}
