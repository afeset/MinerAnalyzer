/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package finalprojectui;


import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import org.python.core.*;
import org.python.util.PythonInterpreter;

/**
 *
 * @author asaf
 */
public class FinalProjectUI {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       
        PythonInterpreter interpreter = new PythonInterpreter(null, new PySystemState());

        PySystemState sys = Py.getSystemState();
        sys.path.append(new PyString("C:\\Users\\dell\\Documents\\GitHub\\MinerAnalyzer\\MinerAnalyzer"));
       // sys.path.append(new PyString("/home/asaf/workspace/FinalProject/mysql-connector-java-5.1.26"));
        //PythonInterpreter interpreter=new PythonInterpreter();
      //  interpreter.execfile("/home/asaf/workspace/FinalProject/src/Configuration/Config.py");
        //interpreter.execfile("/home/asaf/workspace/FinalProject/src/Queries and Reports/Reports/RquestsUserAgentPercentageReport.py");
        interpreter.execfile("C:\\Users\\dell\\Documents\\GitHub\\MinerAnalyzer\\MinerAnalyzer\\DAL\\Test2.py");
        //interpreter.execfile("C:\\Users\\dell\\Documents\\GitHub\\MinerAnalyzer\\MinerAnalyzer\\Utils\\Pair.py");
        //interpreter.execfile("C:\\Users\\dell\\Documents\\GitHub\\Finalproject\\FinalProject\\src\\Reports\\RequestsPercentagePerHeaderReport.py");
        
        
        //PyObject result = interpreter.eval("RquestsUserAgentPercentageReport().loadResults()");
        //PyObject result2 = interpreter.eval("RquestsUserAgentPercentageReport().PrintReportResults()");
        //PyObject result2 = interpreter.eval("RequestsPercentagePerHeaderReport(1,1,1).loadResults()");
        //PyObject result2 = interpreter.eval("Test2().run()");
        //PyObject test=interpreter.eval("Test2()");
        //PyFloat result2 = (PyFloat)test.invoke("run");
        //System.out.println(result2.asDouble());
        //PyList result2 = (PyList) interpreter.eval("Test2().run()");
        //PyObject[] arr=result2.getArray();
        //for(int i=0; i<arr.length; i++)
        //{
        //    System.out.println(arr[i].__getattr__("key"));
        //}
        //System.out.println(result2.__getattr__("key"));
        //result2.invoke("Bla", new PyInteger(5));
        //System.out.println(result2.__getattr__("key"));
       // PyObject result3 = interpreter.eval(result2, PrintReportResults()");
        //System.out.println(result.toString());
        
    }
    
    public static void init() {
        
       String url = "jdbc:mysql://localhost:3306/Project";
        String username = "root";
        String password = "1234";
        Connection connection = null;
        try {
            System.out.println("Connecting database...");
            connection = (Connection) DriverManager.getConnection(url, username, password);
            System.out.println("Database connected!");
        } catch (SQLException e) {
            System.err.println("Cannot connect the database!");
            e.printStackTrace();
        } finally {
            System.out.println("Closing the connection.");
            if (connection != null) try { connection.close(); } catch (SQLException ignore) {}
        }

               }
        
    
}
