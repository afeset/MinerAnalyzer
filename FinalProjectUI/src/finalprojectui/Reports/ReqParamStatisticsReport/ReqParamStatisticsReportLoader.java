/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package finalprojectui.Reports.ReqParamStatisticsReport;

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
public class ReqParamStatisticsReportLoader {
   private Vector<Pair<Integer,String>> _flows;
   private double _requestsWithURIParamTrans;
    private double _requestsWithoutURIParamTrans;
    
    private double _requestsWithURIParamBytes;
    private double _requestsWithoutURIParamBytes;
    
    private double _requestsWithParamEqZeroTrans;
    private double _requestsWithParamEqZeroBytes;
    
    private double _requestsWithParamNotEqZeroTrans;
    private double _requestsWithParamNotEqZeroBytes;
   
   public ReqParamStatisticsReportLoader(Vector<Pair<Integer,String>> flows)
   {
       _flows=flows;
   }
   
   public void load()
   {
       PyInterpreter.getInstance().execFile("Reports\\ReqParamStatisticsReport.py");
       PyObject report=PyInterpreter.getInstance().eval("ReqParamStatisticsReport('begin')");
       report.invoke("loadResults");
       PyFloat res=(PyFloat) report.__getattr__("RequestsWithURIParamTrans");
       _requestsWithURIParamTrans=getFormattedDouble(res.asDouble());
       
       res=(PyFloat) report.__getattr__("RequestsWithURIParamBytes");
       _requestsWithURIParamBytes=getFormattedDouble(res.asDouble());
       
       res=(PyFloat) report.__getattr__("NoParamBytes");
       _requestsWithoutURIParamBytes=getFormattedDouble(res.asDouble());
       
       res=(PyFloat) report.__getattr__("NoParamPercent");
       _requestsWithoutURIParamTrans=getFormattedDouble(res.asDouble());
    
       res=(PyFloat) report.__getattr__("RequestsWithParamEqZeroTrans");
       _requestsWithParamEqZeroTrans=getFormattedDouble(res.asDouble());
       
       res=(PyFloat) report.__getattr__("RequestsWithParamEqZeroBytes");
       _requestsWithParamEqZeroBytes=getFormattedDouble(res.asDouble());
       
       res=(PyFloat) report.__getattr__("RequestsWithParamNotEqZeroTrans");
       _requestsWithParamNotEqZeroTrans=getFormattedDouble(res.asDouble());
       
       res=(PyFloat) report.__getattr__("RequestsWithParamNotEqZeroBytes");
       _requestsWithParamNotEqZeroBytes=getFormattedDouble(res.asDouble());
       
   }

   private double getFormattedDouble(double value)
   {
        DecimalFormat df = new DecimalFormat("#.##");
        String dx=df.format(value);
        return Double.valueOf(dx);
   }
    /**
     * @return the _requestsWithURIParamTrans
     */
    public double getRequestsWithURIParamTrans() {
        return _requestsWithURIParamTrans;
    }

    /**
     * @return the _requestsWithoutURIParamTrans
     */
    public double getRequestsWithoutURIParamTrans() {
        return _requestsWithoutURIParamTrans;
    }

    /**
     * @return the _requestsWithURIParamBytes
     */
    public double getRequestsWithURIParamBytes() {
        return _requestsWithURIParamBytes;
    }

    /**
     * @return the _requestsWithoutURIParamBytes
     */
    public double getRequestsWithoutURIParamBytes() {
        return _requestsWithoutURIParamBytes;
    }

    /**
     * @return the _requestsWithParamEqZeroTrans
     */
    public double getRequestsWithParamEqZeroTrans() {
        return _requestsWithParamEqZeroTrans;
    }

    /**
     * @return the _requestsWithParamEqZeroBytes
     */
    public double getRequestsWithParamEqZeroBytes() {
        return _requestsWithParamEqZeroBytes;
    }

    /**
     * @return the _requestsWithParamNotEqZeroTrans
     */
    public double getRequestsWithParamNotEqZeroTrans() {
        return _requestsWithParamNotEqZeroTrans;
    }

    /**
     * @return the _requestsWithParamNotEqZeroBytes
     */
    public double getRequestsWithParamNotEqZeroBytes() {
        return _requestsWithParamNotEqZeroBytes;
    }

}
