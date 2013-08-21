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
    RequestsPercentagePerHeaderReport("Requests Percentage Per Header Report");   
    
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

