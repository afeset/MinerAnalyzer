/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package finalprojectui.Reports.ItagStatisticsReport;

import finalprojectui.Entities.Pair;
import finalprojectui.Utils.PyInterpreter;
import finalprojectui.Utils.PythonToJavaConverters.PyPairListToPairVectorConverter;
import java.util.List;
import java.util.Vector;
import org.python.core.PyList;
import org.python.core.PyObject;

/**
 *
 * @author dell
 */
public class ItagStatisticsReportLoader {
   private Vector<Pair<Integer,String>> _flows;
   private Vector<Pair<Integer,Double>> _countResults;
   private Vector<Pair<Integer,Double>> _transResults;
   private Vector<Pair<Integer,Double>> _bytesResults;
   
   public ItagStatisticsReportLoader(Vector<Pair<Integer,String>> flows)
   {
       _flows=flows;
   }
   
   public void load()
   {
       PyInterpreter.getInstance().execFile("Reports\\ItagStatisticsReport.py");
       PyObject report=PyInterpreter.getInstance().eval("ItagStatisticsReport()");
       report.invoke("loadResults");
       PyList countRes=(PyList)report.invoke("GetCount");
       _countResults=PyPairListToPairVectorConverter.convert(countRes);
       
       PyList transRes=(PyList)report.invoke("GetTransPer");
       _transResults=PyPairListToPairVectorConverter.convert(transRes);
       
       PyList bytesRes=(PyList)report.invoke("GetBytesPer");
       _bytesResults=PyPairListToPairVectorConverter.convert(bytesRes);
       
   }

    /**
     * @return the _countResults
     */
    public Vector<Pair<Integer,Double>> getCountResults() {
        return _countResults;
    }

    /**
     * @return the _transResults
     */
    public Vector<Pair<Integer,Double>> getTransResults() {
        return _transResults;
    }

    /**
     * @return the _bytesResults
     */
    public Vector<Pair<Integer,Double>> getBytesResults() {
        return _bytesResults;
    }
}
