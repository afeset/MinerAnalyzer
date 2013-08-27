/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package finalprojectui.Reports.UserAgentStatisticsReport;

import finalprojectui.Entities.Pair;
import finalprojectui.Utils.PyInterpreter;
import finalprojectui.Utils.PythonToJavaConverters.PyPairListToPairVectorConverter;
import java.text.DecimalFormat;
import java.util.List;
import java.util.Vector;
import org.python.core.PyFloat;
import org.python.core.PyList;
import org.python.core.PyObject;

/**
 *
 * @author dell
 */
public class UserAgentStatisticsReportLoader {
   private Vector<Pair<Integer,String>> _flows;
   private double _NumberOfTransactionsResult;
   private double _NumberOfBytesResult;
   
   public UserAgentStatisticsReportLoader(Vector<Pair<Integer,String>> flows)
   {
       _flows=flows;
   }
   
   public void load()
   {
       PyInterpreter.getInstance().execFile("Reports\\UserAgentStatisticsReport.py");
       PyObject report=PyInterpreter.getInstance().eval("UseAgentStatisticsReport()");
       report.invoke("loadResults");
       PyFloat transRes=(PyFloat)report.__getattr__("NumberOfTransactionsResult");
       _NumberOfTransactionsResult=getFormattedDouble(transRes.asDouble());
       
       PyFloat bytesRes=(PyFloat)report.__getattr__("NumberOfBytesResult");
       _NumberOfBytesResult=getFormattedDouble(bytesRes.asDouble());
       
   }

   private double getFormattedDouble(double value)
   {
        DecimalFormat df = new DecimalFormat("#.##");
        String dx=df.format(value);
        return Double.valueOf(dx);
   }

    /**
     * @return the _NumberOfTransactionsResult
     */
    public double getNumberOfTransactionsResult() {
        return _NumberOfTransactionsResult;
    }

    /**
     * @return the _NumberOfBytesResult
     */
    public double getNumberOfBytesResult() {
        return _NumberOfBytesResult;
    }
}
