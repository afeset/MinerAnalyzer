/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package finalprojectui;

/**
 *
 * @author dell
 */
public enum ReportType {
    ItagStatisticsReport("Itag Statistics Report"),
    ReqParamStatisticsReport("Requests Params Statistics Report"),
    UserAgentStatisticsReport("User Agent Statistics Report");
    
    private final String name;       

    private ReportType(String s) {
        name = s;
    }

    public boolean equalsName(String otherName){
        return (otherName == null)? false:name.equals(otherName);
    }

    public String toString(){
       return name;
    }
            
}

